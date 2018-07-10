from django.db import models


class Tag(models.Model):
    title = models.TextField(primary_key=True)

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

    @property
    def all_tags(self):
        return [tag for tag in self.tags.all()]

    def __str__(self):
        return self.record_number
