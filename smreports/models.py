from enum import Enum

from django.contrib.auth.models import User
from django.contrib.gis.db.models import BigIntegerField, PointField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

SmartMovingEventType = Enum("SmartMovingEventType", "CREATED_REPORT_POI MODIFIED_REPORT_POI NAVIGATION_REQUEST")
SmartMovingEventType.as_entity = lambda self: reverse("entities:smartmoving_event_types", args=(slugify(self.name),))
# Create your models here.


class ReportType(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Report(models.Model):
    STATE_UNKNOWN = "U"
    STATE_CONFIRMED = "C"
    STATE_RESOLVED = "R"
    STATE_CHOICES = ((STATE_UNKNOWN, "Unknown"), (STATE_CONFIRMED, "Confirmed"), (STATE_RESOLVED, "Resolved"))

    report_type = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    coordinates = PointField(blank=True, db_index=True)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=STATE_CHOICES, default=STATE_UNKNOWN)
    gid = BigIntegerField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.report_type}"


class StatusUpdate(models.Model):

    reportid = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BooleanField(
        null=False, help_text="True if the contribution is confirmed or False if the contribution is solved"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("reportid", "user", "value")

    def __str__(self):
        return f"{self.pk} - {self.user} - {self.reportid}"