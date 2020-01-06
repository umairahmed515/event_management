from django.urls import path
from rest_framework import routers
from events import views
from django.conf.urls import url,include

from simple_event_management_backend.events.views import (
    event_attendance_view
)

app_name = "events"

#Routes define using DRF
router = routers.DefaultRouter()
router.register(r'event_team', views.EventViewSet)
router.register(r'event_details', views.EventDetailViewSet)

#Django Views Routes
urlpatterns = [
    url(r'^', include(router.urls)),
    path("event_attendance/", view=event_attendance_view, name="event_att")
]