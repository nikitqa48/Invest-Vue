from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from django.http import FileResponse
from django_filters.rest_framework import DjangoFilterBackend

class EventViews(ListAPIView):
    pagination_class = None
    queryset = Event.objects.filter(draft=False)
    serializer_class = EventSerializer

class WinnersView(APIView):
    def get(self, request, pk):
        winners = Winners.objects.filter(event=pk)
        serializer = WinnerSerializer(winners, many=True)
        return Response(serializer.data)

