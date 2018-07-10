from django import forms
from django.db import models
import django_filters
from data.models import Record, Tag

STATUS_CHOICES = [
    (year, year)
    for year in range(1770, 2001, 10)
]


class RecordFilter(django_filters.FilterSet):

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects
    )

    class Meta:
        model = Record
        fields = {
            "tags": ["exact"],
            "street": ["icontains"],
            "date": ["year__lt", "year__gt"],
            "description": ["icontains"],
            "caption": ["icontains"],
        }
