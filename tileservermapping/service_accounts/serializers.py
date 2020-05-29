from rest_framework import serializers
from . import models


class ServiceAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ServiceAccount
        fields = ['description', 'expiry', 'is_expired', 'token', 'url']

    expiry = serializers.ReadOnlyField()
    token = serializers.ReadOnlyField()
