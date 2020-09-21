from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from .models import *


class OrganisationSerializer(ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"

class EventSerializer(ModelSerializer):
    date = serializers.DateTimeField()
    partner = OrganisationSerializer(many=True)
    class Meta:
        model = Event
        fields = "__all__"

class WinnerSerializer(ModelSerializer):
    class Meta:
        model = Winners
        fields = '__all__'
    
