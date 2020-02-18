from rest_framework.serializers import ModelSerializer
from .models import *

class ConnectSerializers(ModelSerializer):
    class Meta:
        model = Connect
        fields = [ 'email', 'phone', 'name', 'surname', 'middle_name','organisation']

class InformationSerializers(ModelSerializer):
    class Meta:
        model = InformationForRegion
        fields = ['region', 'power','water','gas', 'heat','water_out']

class NewsSerializers(ModelSerializer):
    class Meta:
        model = News
        fields = ['title','body','publish','created','updated','id','image']

class GreenfieldSerializers(ModelSerializer):
    class Meta:
        model = Greenfield
        fields = ['image','square','form','region','number']