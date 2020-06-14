from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend


class ConnectListView(CreateAPIView):
    serializer_class = ConnectSerializers

class NewsView(ListAPIView):
    queryset = News.objects.order_by('-id')[0:5]
    serializer_class = NewsSerializers


class Allnews(ListAPIView):
    queryset = News.objects.order_by('-id')
    serializer_class = NewsSerializers

class GreenfieldViews(ListAPIView):
    queryset = Greenfield.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    serializer_class = GreenfieldSerializers


class SupportView(ListAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'recipient', 'industry', 'territory', 'form', 'name', 'type_project']


class DetailNews(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

class DetailSupport(RetrieveAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializers

class DocumentView(APIView):
    def get(self, request, pk):
        document = Document.objects.get(id=pk)
        filename = document.file.path
        response = FileResponse(open(filename, 'rb'))
        return response

class ProjectView(ListAPIView):
    queryset =  Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['sum', 'industry', 'time']

class FilterProject(APIView):
    def get(self, request, min, max, industry=None):
        if industry:
            project = Project.objects.filter(sum__range=[min, max], industry=industry)
        else:
            project = Project.objects.filter(sum__range=[min, max])
        serializer = ProjectSerializer(project, many=True, context={"request":request})
        # text = News.objects.filter(body__contains=pk)
        return Response(serializer.data)

