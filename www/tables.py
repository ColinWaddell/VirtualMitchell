from django.urls import reverse
import django_tables2 as tables
from django_tables2.utils import A  # alias for Accessor
from data.models import Record


class RecordTable(tables.Table):

    image_url = tables.TemplateColumn('''
            <div class="record-thumbnail">
                <a 
                    href="http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }}"
                    target="_blank"
                    class="record-thumbnail-img"
                    style="
                        background: url(http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }});
                        background-size: cover;
                    "
                >
                    &nbsp; 
                </a>
                {% if record.caption %}
                    <a href="http://www.mitchelllibrary.org/virtualmitchell/{{ record.image_url }}" class="image-caption">{{ record.caption }}</a>
                {% endif %}
            </div>
        ''',    
        attrs={
            'td': {
                'width': "250",
                'style': '''
                    background: white;
                    padding: 10px;
                    margin: 0;
                '''
            }
        },
        verbose_name=""
    )
    tags = tables.TemplateColumn('''
            {% for tag in record.all_tags %}
                <a href="{% url 'www:search' %}?&tags={{ tag.pk }}">{{ tag }}</a>{% if not forloop.last %}, {% endif %}
            {% endfor %}
        ''',
        attrs={
            'td': {
                'width': "200"
            }
        },
    )
    address = tables.TemplateColumn(
        '''
            {% if record.number %}{{ record.number }}, {% endif %}
            {% if record.street %}{{ record.street }}<br />{% endif %}
            {% if record.area %}{{ record.area }}{% endif %}
        ''',
        attrs={
            'td': {
                'width': "300"
            }
        },
    )
    date = tables.TemplateColumn(
        '''
            {% if record.date_raw %}{{ record.date_raw }}, {% endif %}
        ''',
        attrs={
            'td': {
                'width': "150"
            }
        },
    )

    class Meta:
        model = Record
        template_name = 'django_tables2/bootstrap4.html'
        order_by = 'record_number'
        attrs = {
            'class': 'table records'
        }
        exclude = ("id", )
        fields = (
            "image_url",
            "description",
            "address",
            "date",
            "tags",
        )
