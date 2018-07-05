from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from data.models import Record


class RecordTable(tables.Table):

    # ncr_number = tables.TemplateColumn('<a href="{% url \'ncr:edit\' record.id %}">{{ record }}</a>')

    class Meta:
        model = Record
        template_name = 'django_tables2/bootstrap4.html'
        order_by = 'record_number'
        attrs = {
            'class': 'table table-striped table-bordered table-hover table-sm'
        }
        exclude = ("id", )
        sequence = [
            "record_number",
            "area",
            "date_raw",
            "date",
            "street",
            "number",
            "image_url",
            "description",
            "caption",
        ]
