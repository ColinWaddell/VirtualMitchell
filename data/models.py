from django.db import models
from djgeojson.fields import GeoJSONField, GeometryField

class Location(models.Model):
    place_id = models.IntegerField(primary_key=True)
    osm_id = models.IntegerField()
    lat = models.FloatField()
    lon = models.FloatField()
    bbox = GeometryField()
    geom = GeoJSONField(null=True, blank=True)


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
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    @property
    def all_tags(self):
        return [tag for tag in self.tags.all()]

    def __str__(self):
        return self.record_number
