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

class FilterProject(APIView):
    def get(self, request, number, industry=None, year=None):
        if year:
            print(Project.objects.filter(industry__name='промышленность'))
            project = Project.objects.filter(sum__lte=number, industry=industry).filter(start__lte=year ,finish__gte=year)
        elif industry:
            project = Project.objects.filter(sum__lte=number, industry=industry)
        else:
            project = Project.objects.filter(sum__lte=number)
        serializer = ProjectSerializer(project, many=True, context={"request":request})
        # text = News.objects.filter(body__contains=pk)
        return Response(serializer.data)

class SearchYearView(APIView):
    def get(self, request, year, industry=None):
        if industry:
            project = Project.objects.filter(start__lte=year, finish__gte=year, industry=industry)
        else:
            project = Project.objects.filter(start__lte=year, finish__gte=year)
        serializers = ProjectSerializer(project, many=True, context={'request':request})
        return Response(serializers.data)

class SumYear(APIView):
    def get(self,request, sum, year):
        project = Project.objects.filter(sum__lte=sum,start__lte=year, finish__gte=year, )
        serializers = ProjectSerializer(project, many=True, context={'request': request})
        return Response(serializers.data)

class ContactListView(ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ProjectRequestView(APIView):
    def post(self, request):
        print(request.data.get('project_id'))
        data_project_id = request.data.get('project_id')
        data_organisation = request.data.get('organisation')
        data_phone = request.data.get('phone')
        data_email = request.data.get('email')
        data_name = request.data.get('name')
        data_comment = request.data.get('comment')
        project = Project.objects.get(id=data_project_id)
        request_project = ProjectRequest.objects.create(
            name = data_name,
            project = project,
            phone = data_phone,
            email = data_email,
            organisation = data_organisation,
            comment = data_comment)
        request_project.save()
        print(request_project)
        return Response('ok')