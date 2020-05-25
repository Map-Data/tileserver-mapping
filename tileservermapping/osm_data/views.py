from rest_framework import viewsets, permissions, parsers
from . import models, serializers


class PlanetDumpViewset(viewsets.ModelViewSet):
    queryset = models.PlanetDump.objects.all()
    serializer_class = serializers.PlanetDumpSerializer

    def get_parsers(self):
        if self.request.method == 'POST' or self.request.method == 'PATCH' or self.request.method == 'PUT':
            return [*super(PlanetDumpViewset, self).get_parsers(), parsers.MultiPartParser()]
        else:
            return super().get_parsers()

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.AllowAny()]
        else:
            return super(PlanetDumpViewset, self).get_permissions()
