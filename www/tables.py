from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from data.models import Record


class RecordTable(tables.Table):

    image_url = tables.TemplateColumn('<img src="http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }}" alt="..." class="img-thumbnail">')
    tags = tables.TemplateColumn('''
        {% for tag in record.all_tags %}
            <a href="{% url 'www:search' %}?&tags={{ tag.pk }}">{{ tag }}</a><br />
        {% endfor %}
    ''')

    class Meta:
        model = Record
        template_name = 'django_tables2/bootstrap4.html'
        order_by = 'record_number'
        attrs = {
            'class': 'table table-striped table-bordered table-hover table-sm'
        }
        exclude = ("id", )
