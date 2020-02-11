"""
These URLs are included under / in contrast to the api urls defined in urls_api.py
"""

from django.conf.urls import url
from django.urls import re_path

from tileservermapping.mapping.views import get_server, get_cur_tiles

urlpatterns = [
    re_path(r'^vector/v1/512/all/(?P<z>\d+)/(?P<x>\d+)/(?P<y>\d+)\.(?P<file_ending>[a-zA-Z]+)$', get_server, name='mapping_server'),
    url(r'^cur_tiles.js$', get_cur_tiles , name='mapping_get_cur_tiles'),
]
