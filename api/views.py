from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .serializers import RecordSerializer, TagSerializer
from data.models import Record, Tag


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