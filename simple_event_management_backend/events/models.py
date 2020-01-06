from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField()
    location_address = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title


class EventAttendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='attendants')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attending')

    def __str__(self):
        return "%s - %s" % (self.event, self.attendee)
    