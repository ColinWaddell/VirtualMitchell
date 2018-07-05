from django.conf.urls import url

from . import views

app_name = 'www'
urlpatterns = [
    url(r'^$', views.RecordsView.as_view(), name='index'),
    url(r'^search/', views.RecordsView.as_view(), name='search'),
]
