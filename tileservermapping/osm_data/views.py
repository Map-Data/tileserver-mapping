from rest_framework import viewsets
from . import models, serializers


class PlanetDumpViewset(viewsets.ModelViewSet):
    queryset = models.PlanetDump.objects.all()
    serializer_class = serializers.PlanetDumpSerializer
