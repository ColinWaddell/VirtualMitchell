from django.db import models


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

    def __str__(self):
        return self.record_number


class Tag(models.Model):
    title = models.TextField()

    def __str__(self):
        return self.title


class RecordTag(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (
            self.record,
            self.tag
        )
