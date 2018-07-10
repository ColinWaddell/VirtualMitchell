from data.models import Record, Tag
from rest_framework import serializers


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Record
        read_only = True
        fields = (
            'record_number',
            'date',
            'area',
            'street',
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