from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from simple_event_management_backend.events.models import Event
from .serializers import EventSerializer
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


class EventDetailView(DetailView):

    model = Event

    def get(self, request, *args, **kwargs):
        queryset = Event.objects.all()
        event_names = [eve.title for eve in queryset]
        return HttpResponse(event_names)

event_get_view = EventDetailView.as_view()


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
