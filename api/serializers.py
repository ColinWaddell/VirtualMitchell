from data.models import Record, Tag, Location
from rest_framework import serializers


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        read_only = True
        fields = '__all__' 


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