from django.urls import path

from simple_event_management_backend.events.views import (
    event_get_view
)

app_name = "events"
urlpatterns = [
    #path("create/", view=event_create_view, name="create_ev"),
    path("get_all/", view=event_get_view, name="get_ev"),
    #path("update/", view=event_update_view, name="update_ev"),
    #path("delete/", view=event_delete_view, name="delete_ev")
]