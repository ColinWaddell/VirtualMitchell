from django.contrib import admin
from .models import Record, Tag, Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = (
        'place_id',
        'osm_id',
        'lat',
        'lon'
    )


class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display = (
        'record_number',
        'date_raw',
        'area',
        'street'
    )

admin.site.register(Record, RecordAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Tag)
