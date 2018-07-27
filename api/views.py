from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django_filters.views import FilterView
from .serializers import RecordSerializer, TagSerializer, LocationSerializer
from .filters import LocationFilter
from data.models import Record, Tag, Location


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('place_id', )


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_list(self):
        return {}

    def get_queryset(self):
        term = self.request.query_params.get('term', None)
        if term is not None and len(term) > 2:
            queryset = Tag.objects.filter(title__icontains=term)
            return queryset
        
        raise NotFound