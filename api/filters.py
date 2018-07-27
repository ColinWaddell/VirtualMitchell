import django_filters
from data.models import Location

class LocationFilter(django_filters.FilterSet):

    class Meta:
        model = Location
        fields = {
            "place_id": ["exact", ],
        }
