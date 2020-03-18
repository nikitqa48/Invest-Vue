from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class ConnectListView(CreateAPIView):
    serializer_class = ConnectSerializers

class InformationView(ListAPIView):
    queryset = InformationForRegion.objects.all()
    serializer_class = InformationSerializers

class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class GreenfieldViews(ListAPIView):
    queryset = Greenfield.objects.all()
    serializer_class = GreenfieldSerializers

class BrownfieldViews(ListAPIView):
    queryset = Brownfield.objects.all()
    serializer_class = BrownfieldSerializers

class SupportView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'recipient', 'industry', 'territory']



class DetailNews(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
