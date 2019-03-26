from django.db import models
from rest_framework.reverse import reverse
from djgeojson.fields import GeoJSONField, GeometryField, PointField


class Tag(models.Model):
    title = models.CharField(max_length=50, primary_key=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Record(models.Model):
    record_number = models.CharField(max_length=5)
    area = models.TextField(null=True, blank=True)
    date_raw = models.TextField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    street = models.TextField(null=True, blank=True)
    number = models.TextField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['id']

    @property
    def all_tags(self):
        return [tag for tag in self.tags.all()]

    def __str__(self):
        return self.record_number


class Location(models.Model):
    place_id = models.IntegerField(primary_key=True)
    display_name = models.TextField(default="", blank=True, null=True)
    osm_id = models.BigIntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    geom = GeoJSONField(null=True, blank=True)
    records = models.ManyToManyField(Record, blank=True)

    def __str__(self):
        return str(self.place_id)

    @property
    def record_request_url(self):
        return "%s?place_id=%d" % (
            reverse('api:locationrecords-list'),
            self.place_id
        )
    
    def get_absolute_url(self):
        return reverse('www:locationedit', kwargs={'place_id': self.place_id})


class Report(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    place_id = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)