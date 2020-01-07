from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponse
from simple_event_management_backend.events.models import Event
from .serializers import EventSerializer, EventAttendanceSerializer, EventAttendeesDetailSerializer, EventCreateSerializer
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import UpdateAPIView


class EventViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EventCreateSerializer
        return EventSerializer

    def create(self, request):
        serializer = EventCreateSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   

    def update(self, request, *args, **kwargs):
        event = self.get_object()
        user = request.user
        if request.user == event.owner:
            serializer = EventCreateSerializer(event, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request, pk=None):
        event = self.get_object()
        if request.user == event.owner:
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

class EventAttendanceViewSet(UpdateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EventAttendanceSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = { 'user_id': request.data['user_id'], 'event_id': request.data['event_id']}
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        serialized_data = EventSerializer(data)

        return Response(serialized_data.data, status=status.HTTP_200_OK)

event_attendance_view = EventAttendanceViewSet.as_view()

class EventDetailViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Event.objects.all()
    serializer_class = EventAttendeesDetailSerializer