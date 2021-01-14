from rest_framework.serializers import ModelSerializer, StringRelatedField, PrimaryKeyRelatedField
from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from .models import *

class ConnectSerializers(ModelSerializer):
    class Meta:
        model = Connect
        fields = [ 'email', 'phone', 'name', 'surname', 'middle_name', 'organisation', 'text']



class NewsSerializers(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=NewsTranslate)
    class Meta:
        model = NewsTranslate
        fields = '__all__'

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


class SupportSerializers(TranslatableModelSerializer):
    industry = StringRelatedField(many=True)
    type_project = StringRelatedField(many=True)
    translations = TranslatedFieldsField(shared_model=SupportTranslate)
    class Meta:
        model = SupportTranslate
        fields = ['id', 'recipient', 'name', 'type','form','translations', 'industry', 'type_project']

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


