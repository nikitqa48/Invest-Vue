from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from .models import *


class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ('video',)

class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"

class EventSerializer(ModelSerializer):
    date = serializers.DateTimeField()
    video = VideoSerializer(many=True)
    partner = OrganisationSerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"

class WinnerSerializer(ModelSerializer):
    class Meta:
        model = Winners
        fields = '__all__'
    
