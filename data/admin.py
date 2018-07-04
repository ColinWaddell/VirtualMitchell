from django.contrib import admin
from .models import Record, RecordTag, Tag


class RecordTagInline(admin.TabularInline):
    model = RecordTag


class RecordTagAdmin(admin.ModelAdmin):
    model = RecordTag


class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display = (
        'record_number',
        'date_raw',
        'area',
        'street'
    )
    inlines = [RecordTagInline]


admin.site.register(Record, RecordAdmin)
admin.site.register(RecordTag, RecordTagAdmin)
admin.site.register(Tag)