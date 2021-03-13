from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

class GetDocumentView(APIView):
    def get(self, request):
        section = Section.objects.all()
        serialize_section = SectionSerialize(section, many=True, context={'request':request})
        subesections = SubSection.objects.all()
        documents = File.objects.all()
        serialize = SubSectionSerialize(subesections, many=True)
        docs = DocsSerialize(documents, many=True, context={'request':request})
        return Response({'subsection':serialize.data, 'files':docs.data, 'section':serialize_section.data})