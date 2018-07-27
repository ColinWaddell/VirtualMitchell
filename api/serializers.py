from data.models import Record, Tag, Location
from rest_framework import serializers

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        read_only = True
        fields = (
            'place_id',
            'lat',
            'lon',
            'bbox',
            'geom',
            'record_count'
        )


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        read_only = True
        fields = (
            'record_number',
            'date',
            'area',
            'street',
            'location'
        )

class TagSerializer(serializers.HyperlinkedModelSerializer):
    
    label = serializers.ReadOnlyField(source='title')
    value = serializers.ReadOnlyField(source='title')

    class Meta:
        model = Tag
        read_only = True
        fields = (
            'label',
            'value'
        )