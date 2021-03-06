from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.db.models import Max
from django.forms.models import modelform_factory
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.forms import TextInput, DateInput, Textarea

from data.models import Record, Location, Report

from django_tables2 import RequestConfig
from leaflet.forms.widgets import LeafletWidget

from .tables import RecordTable, LocationTable
from .filters import RecordFilter, LocationFilter
from .forms import RecordLocationForm

from extra_views.advanced import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSet
from extra_views.generic import GenericInlineFormSet

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class LocationUpdate(LoginRequiredMixin, UpdateView):
    model = Location
    form_class =  modelform_factory(
        Location,
        fields=(
            'display_name',
            'lat',
            'lon',
            'geom',
        ),
        widgets={
            'geom': LeafletWidget()
        }
    )
    template_name = 'location-form.html'
    pk_url_kwarg = 'place_id'


class RecordUpdate(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = modelform_factory(
        Record,
        exclude=(
            'record_number',
            'image_url',
            'date_raw'
        ),
        widgets={
            "area": TextInput,
            "street": TextInput,
            "number": TextInput,
            "caption": TextInput,
            "image_url": TextInput,
            "description": TextInput,
        },
    )
    template_name = 'record-form.html'
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        record = Record.objects.get(id=self.kwargs['id'])
        form_valid_url = super().form_valid(form)
        if record.date != form.cleaned_data['date']:
            record.date = form.cleaned_data['date']
            record.date_raw = form.cleaned_data['date'].strftime("%b. %Y")
            record.save()
        return form_valid_url

    def get_success_url(self):
        return reverse_lazy('www:recordedit', kwargs=self.kwargs)


class RecordsView(SingleTableMixin, FilterView):
    table_class = RecordTable
    model = Record
    template_name = 'records.html'
    paginate_by = 25
    filterset_class = RecordFilter


class RecordLocationAppView(LoginRequiredMixin, FormView):
    template_name = 'record-location-edit.html'
    form_class = RecordLocationForm

    def get_context_data(self, **kwargs):
        context = super(RecordLocationAppView, self).get_context_data(**kwargs)
        record_id = self.kwargs['id']
        context["record"] = Record.objects.get(id=record_id)
        return context

    def get_success_url(self):
        return reverse_lazy('www:recordedit', kwargs=self.kwargs)

    def form_valid(self, form):
        # TODO need to generate date_raw on save
        form.update_location()
        return super().form_valid(form)

    def get_initial(self):
        record_id = self.kwargs['id']

        try:
            # getrecordor404
            record = Record.objects.get(id=record_id)
            place = record.location_set.first()
            place_id = place.place_id if place else None

        except (IndexError, Record.DoesNotExist):
            place_id = None

        return {
            'record_id': record_id,
            'place_id': place_id,
        }


class ReportCreate(CreateView):
    model = Report
    template_name = 'record-report.html'
    fields = ('record', 'place_id', 'comment')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        record_id = self.kwargs['record_id']
        context["record"] = Record.objects.get(id=record_id)
        return context

    def get_initial(self):
        # Get the initial dictionary from the superclass method
        initial = super().get_initial()
        initial = initial.copy()
        initial['record'] = self.kwargs['record_id']
        return initial

    def get_success_url(self):
        try:
            return self.request.GET["return"]
        except KeyError:
            return reverse_lazy('www:index')


class MapView(SingleTableMixin, FilterView):
    model = Location
    template_name = 'map.html'
    filterset_class = LocationFilter
