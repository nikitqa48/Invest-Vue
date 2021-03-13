from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from .models import *

class SectionSerialize(ModelSerializer):
    class Meta:
        model = Section
        fields = ('name', 'text', 'slug')

class SubSectionSerialize(ModelSerializer):
    section = SectionSerialize()
    class Meta:
        model = SubSection
        fields = '__all__'

class SubSectionName(ModelSerializer):
    class Meta:
        model = SubSection
        fields = ('name',)
class DocsSerialize(ModelSerializer):
    subsection = SubSectionName()
    class Meta:
        model = File
        fields = '__all__'