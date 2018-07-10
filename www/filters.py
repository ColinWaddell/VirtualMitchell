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

    date__year__lt = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES,
        empty_label="Before the year..."
    )

    date__year__gt = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES,
        empty_label="After the year..."
    )

    class Meta:
        model = Record
        fields = {
            "tags": ["exact"],
            "street": ["icontains"],
            "date": ['year__lt', 'year__gt'],
            "description": ["icontains"],
            "caption": ["icontains"],
        }
