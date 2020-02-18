"""tileservermapping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/2.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Tileserver-Mapping Api",
        description="Api to control the management of tileserver, their status and statistics",
        default_version="v1",
        contact=openapi.Contact("Nils Rokita, Finn-Thorben Sell"),
        license=openapi.License("MIT", "https://github.com/Map-Data/tileserver-mapping/blob/master/LICENSE")
    ),
    public=True,
    permission_classes=()
)


urlpatterns = [
    path("api/<str:version>/", include("tileservermapping.mapping.urls")),
    path("mappings/", include("tileservermapping.mapping.urls")),   # included for compatibility to old url schema

    path("admin/", admin.site.urls),
    path("schema<str:format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),

    path("", RedirectView.as_view(url="/docs"))
]
