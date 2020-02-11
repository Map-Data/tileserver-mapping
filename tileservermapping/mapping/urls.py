from django.conf.urls import url
from django.urls import path, include
from dynamic_rest import routers

from .views import get_server, get_cur_tiles
from . import views

urlpatterns = [
    url(r'^vector/v1/512/all/(\d+)/(\d+)/(\d+)\.([a-zA-Z]+)$', get_server, name='mapping_server'),
    url(r'^cur_tiles.js$', get_cur_tiles , name='mapping_get_cur_tiles'),
]


router = routers.DefaultRouter()
router.register(r"servers", views.ServerViewSet)

urlpatterns += [
    path("", include(router.urls))
]
