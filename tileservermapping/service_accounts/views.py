from rest_framework import views, viewsets, mixins, generics, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.request import Request
from . import serializers
from . import models
from . import permission_classes


class ServiceAccountViewset(viewsets.ModelViewSet):
    queryset = models.ServiceAccount.objects.all()
    serializer_class = serializers.ServiceAccountSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        elif self.action == 'retrieve' or self.action == 'renew':
            return [permission_classes.RequestAuthToItself()]
        else:
            return super(ServiceAccountViewset, self).get_permissions()

    @action(methods=['POST'], detail=True)
    def renew(self, request: Request, version: str, pk: str):
        obj = self.get_object()     # type: models.ServiceAccount
        obj.renew()
        obj.save()
        return self.retrieve(request)
