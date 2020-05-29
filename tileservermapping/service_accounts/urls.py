from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('serviceaccounts', views.ServiceAccountViewset)

urlpatterns = router.urls
