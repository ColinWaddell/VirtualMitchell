from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.filterset import FilterSet
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django_filters.views import FilterView
from .serializers import RecordSerializer, TagSerializer
from .filters import LocationFilter
from data.models import Record, Tag, Location


class LocationRecordsViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def _build_record_query(self, query_params):
        record_query = self.request.query_params.copy()
        try:
            del record_query['place_id']
        except KeyError:
            # must already be missing
            pass

        record_query_formatted = {
            key.replace('records__', '') : value
            for (key, value) in record_query.items()
        }

        if ('tags' in record_query_formatted):
            record_query_formatted['tags__in'] = self.request.query_params.getlist('records__tags')
            del record_query_formatted['tags']

        return record_query_formatted

    def get_queryset(self):
        place_id = self.request.query_params.get('place_id', None)
        if place_id is not None:
            queryset = Location.objects.get(place_id=place_id)
            record_query = self._build_record_query(self.request.query_params)
            record_filtered = queryset.records.filter(**record_query)

            if len(record_filtered):
                return record_filtered

        raise NotFound


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
