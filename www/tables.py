from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from data.models import Record


class RecordTable(tables.Table):

    image_url = tables.TemplateColumn('''
        <a href="http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }}" target="_blank">
            <img src="http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }}" alt="{{ record.description }}" class="img-thumbnail col-12">
        </a>
    ''')
    tags = tables.TemplateColumn('''
        <ul>
            {% for tag in record.all_tags %}
                <li><a href="{% url 'www:search' %}?&tags={{ tag.pk }}">{{ tag }}</a></li>
            {% endfor %}
        </ul>
    ''')

    class Meta:
        model = Record
        template_name = 'django_tables2/bootstrap4.html'
        order_by = 'record_number'
        attrs = {
            'class': 'table table-striped table-bordered table-hover table-sm'
        }
        exclude = ("id", )
