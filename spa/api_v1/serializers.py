import datetime

from rest_framework import serializers
from .models import Event


class EventPreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'title',
            'date',
            'url',
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M", input_formats=None)

    class Meta:
        model = Event
        fields = '__all__'
