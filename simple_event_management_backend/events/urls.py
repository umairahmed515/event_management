from django.urls import path
from rest_framework import routers
from events import views
from django.conf.urls import url,include

from simple_event_management_backend.events.views import (
    event_get_view
)

app_name = "events"

#Routes define using DRF
router = routers.DefaultRouter()
router.register(r'event_team', views.EventViewSet)

#Django Views Routes
urlpatterns = [
    #path("create/", view=event_create_view, name="create_ev"),
    url(r'^', include(router.urls)),
    path("get_all/", view=event_get_view, name="get_ev"),
    #path('event_team/<int:pk>/', views.event_detail),
    #path("update/", view=event_update_view, name="update_ev"),
    #path("delete/", view=event_delete_view, name="delete_ev")
]