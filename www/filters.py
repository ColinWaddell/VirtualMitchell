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

    def __init__(self, *args, **kwargs):
        super(RecordFilter, self).__init__(*args, **kwargs)
        self.filters['street__icontains'].label = "Street"
        self.filters['date__year__lt'].label = "Year (less than)"
        self.filters['date__year__gt'].label = "Year (greater than)"
        self.filters['description__icontains'].label = "Description"
        self.filters['caption__icontains'].label = "Caption"

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

    def __init__(self, *args, **kwargs):
        super(LocationFilter, self).__init__(*args, **kwargs)
        self.filters['records__street__icontains'].label = "Street"
        self.filters['records__date__year__lt'].label = "Year (less than)"
        self.filters['records__date__year__gt'].label = "Year (greater than)"
        self.filters['records__description__icontains'].label = "Description"
        self.filters['records__caption__icontains'].label = "Caption"

    class Meta:
        model = Location
        fields = {
            "records__tags": ["exact"],
            "records__street": ["icontains"],
            "records__date": ["year__lt", "year__gt"],
            "records__description": ["icontains"],
            "records__caption": ["icontains"],
        }
