from django.conf.urls import url

from .views import mapping, get_server, get_cur_tiles

urlpatterns = [
    url(r'^(\d+)/(\d+)/(\d+)\.([a-zA-Z]+)$', mapping, name='mapping_mapping'),
    url(r'^vector/v1/512/all/(\d+)/(\d+)/(\d+)\.([a-zA-Z]+)$', get_server, name='mapping_server'),
    url(r'^cur_tiles.js$', get_cur_tiles , name='mapping_get_cur_tiles'),
]
