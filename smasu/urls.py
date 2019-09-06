"""smasu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# from rest_framework.urlpatterns import format_suffic_patterns

extra_patterns = [
    path("", include("spusers.urls")),
    path("", include("spevents.urls")),
    path("", include("splots.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("smartparking/", include(extra_patterns)),
    path("health/", include("smhealth.urls")),
]
