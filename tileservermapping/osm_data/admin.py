from django.contrib import admin
from . import models

admin.site.register(models.PlanetDump)
admin.site.register(models.SqlDump)