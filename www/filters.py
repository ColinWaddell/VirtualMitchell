import django_filters
from data.models import Record


class RecordFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = {
            "record_number": ["icontains"],
            "area": ["exact"],
            "date_raw": ["icontains"],
            "date": ["icontains"],
            "street": ["icontains"],
            "number": ["icontains"],
            "image_url": ["icontains"],
            "description": ["icontains"],
            "caption": ["icontains"],
        }
