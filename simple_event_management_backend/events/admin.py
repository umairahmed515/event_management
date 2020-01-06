from django.contrib import admin
from simple_event_management_backend.events.models import Event
from simple_event_management_backend.events.models import EventAttendance


admin.site.register(Event)
admin.site.register(EventAttendance)