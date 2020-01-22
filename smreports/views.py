from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import parsers, renderers, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from smasu.authentication import IsCreateView, IsListView, IsSuperUserOrStaff, TokenAuthenticationInQuery
from smasu.helpers import as_entity
from smasu.models import Application
from smevents.models import Event
from smrouter.utils import Router

from .models import Report, SmartMovingEventType, StatusUpdate
from .parsers import ReportPoiGeoJSONParser
from .renderers import ReportPoiGeoJSONRenderer
from .serializers import ReportSerializer, StatusUpdateSerializer


class IsSmartMovingUser(IsAuthenticated):
    def has_permission(self, request, view):
        return super().has_permission(request, view) and request.user.smartmovingprofile is not None


class ReportsView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthenticationInQuery)
    permission_classes = (IsSuperUserOrStaff | ((IsCreateView | IsListView) & IsSmartMovingUser),)
    parser_classes = (ReportPoiGeoJSONParser, parsers.FormParser)
    serializer_class = ReportSerializer
    renderer_classes = [ReportPoiGeoJSONRenderer, renderers.BrowsableAPIRenderer]

    @receiver(post_save, sender=Report)
    def create_event_report(sender, instance, **kwargs):

        with transaction.atomic():
            if kwargs.get("created", False):
                Event(
                    application=Application.objects.get(name="SmartMovingApp"),
                    e_type=as_entity(SmartMovingEventType.CREATED_REPORT_POI),
                    agent=as_entity(instance.user_created),
                    position=instance.coordinates,
                ).save()
                instance.gid = Router.get_nearest_edge(instance.coordinates)
                instance.save()
        return Response(status=200)


class StatusUpdatesView(viewsets.ModelViewSet):
    queryset = StatusUpdate.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthenticationInQuery)
    permission_classes = (IsSuperUserOrStaff | ((IsCreateView | IsListView) & IsSmartMovingUser),)
    serializer_class = StatusUpdateSerializer

    @receiver(post_save, sender=StatusUpdate)
    def create_event(sender, instance, **kwargs):
        report = instance.reportid
        count_true = int(StatusUpdate.objects.filter(value=True, reportid=report).count())
        count_false = int(StatusUpdate.objects.filter(value=False, reportid=report).count())
        if count_true >= 0 and count_true < 3 and count_false >= 0 and count_false < 3:
            report.status = Report.STATE_UNKNOWN
        elif count_false > 0 and count_false < 3 and count_true >= 3:
            report.status = Report.STATE_UNKNOWN
        elif count_false == 3 and count_true >= 0:
            report.status = Report.STATE_RESOLVED
        if count_true >= 3 and count_false == 0:
            report.status = Report.STATE_CONFIRMED
        report.modified = instance.created
        report.save()
        with transaction.atomic():
            if kwargs.get("created", False):
                Event(
                    application=Application.objects.get(name="SmartMovingApp"),
                    e_type=as_entity(SmartMovingEventType.MODIFIED_REPORT_POI),
                    agent=as_entity(instance.user),
                    position=instance.reportid.coordinates,
                ).save()
        return Response(status=200)