from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from .serializers import *
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend


class ConnectListView(CreateAPIView):
    serializer_class = ConnectSerializers

class NewsView(ListAPIView):
    pagination_class = None
    queryset = NewsTranslate.objects.order_by('-publish')[0:5]
    serializer_class = NewsSerializers


class Allnews(ListAPIView):
    queryset = NewsTranslate.objects.order_by('-publish')
    serializer_class = NewsSerializers

class GreenfieldViews(ListAPIView):
    pagination_class = None
    queryset = Greenfield.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    serializer_class = GreenfieldSerializers


class SupportView(ListAPIView):
    pagination_class = None
    queryset = SupportTranslate.objects.all()
    serializer_class = SupportSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type', 'recipient', 'industry', 'territory', 'form', 'type_project']


class DetailNews(RetrieveAPIView):
    queryset = NewsTranslate.objects.all()
    serializer_class = NewsSerializers

class DetailSupport(RetrieveAPIView):
    queryset = SupportTranslate.objects.all()
    serializer_class = SupportSerializers

class DocumentView(APIView):
    def get(self, request, pk):
        document = Document.objects.get(id=pk)
        filename = document.file.path
        response = FileResponse(open(filename, 'rb'))
        return response


class ProjectView(ListAPIView):
    pagination_class = None
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
    pagination_class = None
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

class ProjectRequestView(APIView):
    def post(self, request):
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

class EventRequestView(APIView):
    def post(self, request):
        data_organisation = request.data.get('organisation')
        data_phone = request.data.get('phone')
        data_email = request.data.get('email')
        data_name = request.data.get('name'),
        data_secondame = request.data.get('second_name'),
        data_profile = request.data.get('profile')
        data_role = request.data.get('role')
        data_transfer = request.data.get('transfer')
        request_event = Event.objects.create(
            name = data_name,
            profile = data_profile,
            role = data_role,
            phone = data_phone,
            email = data_email,
            second_name = data_secondame,
            organisation = data_organisation,
            transfer = data_transfer)
        request_event.save()
        return Response('ok')



class CopyNews(APIView):
    def get(self, request):
        allnews = News.objects.all()
        for item in allnews:
            new = NewsTranslate(
                title = item.title,
                image = item.image,
                slug = item.slug,
                body = item.body,
                publish = item.publish,
                updated = item.updated
            )
            new.save()
        return Response('ok')

class CopySupport(APIView):
    def get(self, request):
        supports = Support.objects.all()
        for sup in supports:
            supp = SupportTranslate(
            name=sup.name,
            territory = sup.territory,
            recipient = sup.recipient,
            type=sup.type,
            implementation=sup.implementation,
            authority=sup.authority,
            form=sup.form,
            target=sup.target,
            nalog=sup.nalog,
            expenses=sup.expenses,
            project_name=sup.project_name,
            program_name=sup.program_name,
            npa=sup.npa,
            organisation=sup.organisation,
            condition=sup.condition,
            category=sup.category,
            loan_time=sup.loan_time,
            property_rate=sup.property_rate,
            profit=sup.profit,
            transport=sup.transport,
            land=sup.land,
            nds=sup.nds,
            money=sup.money,
            summ=sup.summ,
            percent=sup.percent
            )
            supp.save()
            supp.industry.set(sup.industry.all()) 
            supp.type_project.set(sup.type_project.all())
        return Response('ok')

class CopyGreenfield(APIView):
    def get(self, request):
        greenfields = Greenfield.objects.all()
        for item in greenfields:
            greenfield = GreenfieldTranslate(
                region = item.region,
                number_territory = item.number_territory,
                image = item.image,
                number=item.number,
                description = item.description,
                territory = item.territory,
                type = item.type,
                square = item.square,
                power = item.power,
                water = item.water,
                gas = item.gas,
                heat = item.heat,
                water_out = item.water_out,
                danger = item.danger,
                category = item.category,
                desired = item.desired,
                customs_priveleges = item.customs_priveleges,
                territory_priveleges = item.territory_priveleges,
                nalog = item.nalog
            )
            greenfield.save()
            greenfield.form.set(item.form.all())
        return Response('ok')

class GetSupport(APIView):
    def get(self, request):
        support = SupportTranslate.objects.all()
        serialize = SupportSerialize(support, many=True)
        return Response(serialize.data)       

# class CopyProject(APIView):
#     def get(self, request):
#         project = Project.objects.all()
#         for item in project:
#             projects = ProjectTranslate(
#                 industry = item.industry,
#                 start = item.start,
#                 finish = item.finish,
#                 sum = item.sum,
#                 image = item.image,
#                 help = item.help,
#                 name = item.name,
#                 body = item.body,
#                 now = item.now
#             )
#             projects.save()
#         return Response('ok')