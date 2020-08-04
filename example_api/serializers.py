from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from .models import *

class ConnectSerializers(ModelSerializer):
    class Meta:
        model = Connect
        fields = [ 'email', 'phone', 'name', 'surname', 'middle_name', 'organisation', 'text']



class NewsSerializers(ModelSerializer):
    class Meta:
        model = News
        fields = ['title','body','publish','created','updated','id','image', 'slug']

class GreenfieldSerializers(ModelSerializer):
    form = StringRelatedField(many=True)
    class Meta:
        model = Greenfield
        fields = ['image','square','form','region','number', 'type', 'power', 'water', 'gas',
                  'heat', 'water_out', 'description', 'danger', 'category',
                  'desired', 'territory', 'number_territory', 'customs_priveleges', 'territory_priveleges', 'nalog']

class IndustrySerializers(ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name']


class SupportSerializers(ModelSerializer):
    industry = StringRelatedField(many=True)
    type_project = StringRelatedField(many=True)
    class Meta:
        model = Support
        fields = ['id', 'recipient', 'name', 'type','form',
                'organisation', 'category', 'industry',
                'property_rate', 'profit', 'transport',
                'land', 'nds', 'expenses', 'condition', 'territory',
                'implementation', 'type_project', 'target', 'authority',
                'project_name', 'program_name', 'npa', 'money', 'summ', 'loan_time', 'percent']


class ProjectSerializer(ModelSerializer):
    industry = StringRelatedField()
    class Meta:
        model = Project
        fields = ['image','industry', 'name',  'sum', 'now', 'body', 'start', 'finish', 'id', 'help']

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'position', 'image', 'role']

class ProjectIdSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id']

class RequestSerializer(ModelSerializer):
    project = PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = ProjectRequest
        fields = ['name', 'organisation', 'phone', 'email', 'comment', 'project']



