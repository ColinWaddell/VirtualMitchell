from django.contrib import admin
from .models import Record, Tag, Location
from leaflet.admin import LeafletGeoAdmin

class LocationAdmin(LeafletGeoAdmin):
    model = Location
    filter_horizontal = ['records']


class LocationInline(admin.TabularInline):
    model = Location.records.through


class RecordAdmin(admin.ModelAdmin):
    model = Record
    inlines = [LocationInline]

admin.site.register(Record, RecordAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tag)
