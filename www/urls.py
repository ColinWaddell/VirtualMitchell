from django.conf.urls import url

from . import views

app_name = 'www'
urlpatterns = [
    url(r'^$', views.RecordsView.as_view(), name='index'),
    url(r'^search/', views.RecordsView.as_view(), name='search'),
    url(r'^map/', views.MapView.as_view(), name='map'),
    url(r'^record/location/edit/(?P<id>[\w-]+)$', views.RecordLocationAppView.as_view(), name='recordlocation'),
    url(r'^record/edit/(?P<id>[\w-]+)$', views.RecordUpdate.as_view(), name='recordedit'),
    url(r'^location/edit/(?P<place_id>[\w-]+)$', views.LocationUpdate.as_view(), name='locationedit'),
]
