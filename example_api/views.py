from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from .serializers import *


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

class DetailNews(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers