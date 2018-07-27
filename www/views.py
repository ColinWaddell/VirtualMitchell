from django.shortcuts import render
from django_tables2 import RequestConfig
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Max
from data.models import Record, Location
from .tables import RecordTable, LocationTable
from .filters import RecordFilter, LocationFilter

from extra_views.advanced import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class RecordsView(SingleTableMixin, FilterView):
    table_class = RecordTable
    model = Record
    template_name = 'records.html'
    paginate_by = 25
    filterset_class = RecordFilter


class MapView(SingleTableMixin, FilterView):
    model = Location
    template_name = 'map.html'
    filterset_class = LocationFilter
