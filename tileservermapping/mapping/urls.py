from django.urls import path, include, re_path
from rest_framework import routers

from . import views
from .views import get_server, get_cur_tiles

router = routers.DefaultRouter()
router.register(r"servers", views.ServerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^vector/v1/512/all/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)\.(?P<file_ending>[a-zA-Z]+)$', get_server, name='mapping_server'),
    path(r'cur_tiles.js', get_cur_tiles , name='mapping_get_cur_tiles'),
]
