from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ProfileListView(ModelViewSet):
    queryset = Connect.objects.all()
    serializer_class = ConnectSerializers

class InformationView(ModelViewSet):
    queryset = InformationForRegion.objects.all()
    serializer_class = InformationSerializers

inform_list = InformationView.as_view({
    'get': 'list',
})

class NewsView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

news_list = NewsView.as_view({
    'get': 'list',
})
class GreenfieldViews(ModelViewSet):
    queryset = Greenfield.objects.all()
    serializer_class = GreenfieldSerializers

green_list = GreenfieldViews.as_view({
    'get':'list'
})
