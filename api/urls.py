from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tags', views.TagViewSet)
router.register(r'locationrecords', views.LocationRecordsViewSet, base_name='locationrecords')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
app_name = "api"
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
