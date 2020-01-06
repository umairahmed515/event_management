from rest_framework import serializers
from simple_event_management_backend.events.models import Event
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

class EventSerializer(serializers.ModelSerializer):
    #event_owner = serializers.CharField(source='owner.username')
    class Meta:
        model = Event
        fields = ('title', 'description','datetime','location_address','owner')
    
    def create(self, validated_data):
        print(validated_data)
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