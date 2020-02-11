"""
These URLs are included under /<version>/api/ and are therefore api urls
"""

from django.urls import path, include
from dynamic_rest import routers

from . import views

router = routers.DefaultRouter()
router.register(r"servers", views.ServerViewSet)

urlpatterns = [
    path("", include(router.urls))
]
