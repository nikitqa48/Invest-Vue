from rest_framework.serializers import ModelSerializer
from .models import *

class ConnectSerializers(ModelSerializer):
    class Meta:
        model = Connect
        fields = [ 'email', 'phone', 'name', 'surname', 'middle_name', 'organisation']

class InformationSerializers(ModelSerializer):
    class Meta:
        model = InformationForRegion
        fields = ['region', 'power','water','gas', 'heat','water_out']

class NewsSerializers(ModelSerializer):
    class Meta:
        model = News
        fields = ['title','body','publish','created','updated','id','image', 'slug']

class GreenfieldSerializers(ModelSerializer):
    class Meta:
        model = Greenfield
        fields = ['image','square','form','region','number']


class IndustrySerializers(ModelSerializer):
    class Meta:
        model = Industry
        fields = ['name']


class SupportSerializers(ModelSerializer):
    industry = IndustrySerializers()
    class Meta:
        model = Support
        fields = ['recipient', 'name', 'type',
                'organisation', 'category', 'industry',
                'property_rate', 'profit', 'transport',
                'land', 'nds', 'expenses', 'condition', 'territory']

