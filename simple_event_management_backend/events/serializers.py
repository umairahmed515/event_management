from rest_framework import serializers
from simple_event_management_backend.events.models import Event
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ('id', 'title', 'description','datetime','location_address','owner')
    
    def create(self, validated_data):
        user = User.objects.get(username=validated_data['owner'])
        event = Event(
            title=validated_data['title'],
            description=validated_data['description'],
            datetime=datetime.datetime.now(),
            location_address=validated_data['location_address'],
            owner=user
        )
        event.save()
        return event
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.datetime = validated_data.get('datetime', instance.datetime)
        instance.location_address = validated_data.get('location_address', instance.location_address)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance