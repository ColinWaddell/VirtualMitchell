from django import forms
from django.db import models
import django_filters
from data.models import Record, Tag, Location

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


class LocationFilter(django_filters.FilterSet):

    class Meta:
        model = Location
        fields = {
            "place_id": ["exact", ],
            "records__tags": ["exact"],
            "records__street": ["icontains"],
            "records__date": ["year__lt", "year__gt"],
            "records__description": ["icontains"],
            "records__caption": ["icontains"],
        }