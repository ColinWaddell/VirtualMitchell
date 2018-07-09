from django import forms
from django.db import models
import django_filters
from data.models import Record, Tag


class RecordFilter(django_filters.FilterSet):

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects
    )

    class Meta:
        model = Record
        fields = {
            "tags": ["exact"],
            "date": ['lt', 'gt'],
            "description": ["icontains"],
            "caption": ["icontains"],
        }
