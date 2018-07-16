from django.contrib import admin
from .models import Record, Tag, Location


class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display = (
        'record_number',
        'date_raw',
        'area',
        'street'
    )

admin.site.register(Record, RecordAdmin)
admin.site.register(Tag)
admin.site.register(Location)