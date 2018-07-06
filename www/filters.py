from django import forms
from django.db import models
import django_filters
from data.models import Record, Tag


class RecordFilter(django_filters.FilterSet):

    class Meta:
        model = Record
        fields = {
            "record_number": ["icontains"],
            "date": ['exact', 'lte', 'gte'],
            "area": ["exact"],
            "street": ["icontains"],
            "number": ["icontains"],
            "image_url": ["icontains"],
            "description": ["icontains"],
            "caption": ["icontains"],
            "tags": ['exact']
        }
        filter_overrides = {
            models.DateField: {'filter_class': django_filters.DateFilter},
        }
