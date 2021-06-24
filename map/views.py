from os import name
from example_api.models import Greenfield, GreenfieldTranslate
from rest_framework.views import APIView
from rest_framework.response import Response
from example_api .serializers import GreenfieldSerializers
from django_filters import rest_framework as filters
from django_filters import CharFilter
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend


def filter(queryset, url, value):
    qs = queryset.translated(**{url:value})
    boolean = ['gas', 'power', 'water', 'heat', 'water_out', 'customs_priveleges', 'territory_priveleges', 'nalog']
    if url in boolean:
        kwargs = {'translations__{}__isnull'.format(url):True}
        args = {'translations__{}'.format(url):''}
        qs = queryset.exclude(**(kwargs)).exclude(**(args))
    if url == 'square':
        qs = queryset.translated(square__lte=value)
    if not value:
        return queryset
    return qs

class ProductFilter(filters.FilterSet):
    form = CharFilter(field_name='form__title', lookup_expr='contains')
    gas = CharFilter(method=filter)
    water = CharFilter(method=filter)
    heat =  CharFilter(method=filter)
    power = CharFilter(method=filter)
    water_out = CharFilter(method=filter)
    customs_priveleges =  CharFilter(method=filter)
    territory_priveleges = CharFilter(method=filter)
    water_out = CharFilter(method=filter)
    nalog = CharFilter(method=filter)
    class Meta:
        model = GreenfieldTranslate
        fields = ['translations__type','translations__square', 'translations__territory', 
        'form', 'translations__danger', 
        'translations__category',
         'translations__desired', 'gas','water', 'heat', 'power', 'water_out', 'customs_priveleges', 'territory_priveleges', 'nalog', ]


class FilterMap(ListAPIView):
    queryset = GreenfieldTranslate.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    pagination_class = None
    serializer_class = GreenfieldSerializers
   