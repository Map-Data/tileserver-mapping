from django.urls import path, include, re_path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"servers", views.ServerViewSet)

urlpatterns = [
    path("", include(router.urls)),
    re_path(r'^vector/v1/512/all/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)\.(?P<file_ending>[a-zA-Z]+)$',
            views.GetServerView.as_view(), name='mapping_server'),
    path(r'cur_tiles.js', views.get_cur_tiles , name='mapping_get_cur_tiles'),
]
