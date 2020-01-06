from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models

class Event(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField()
    location_address = models.CharField(max_length=255)

    def __str__(self):
        return self.title