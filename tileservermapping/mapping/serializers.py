from rest_framework import serializers

from . import models


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        fields = ["id", "name", "x", "y", "z", "active", "scheme", "host", "url", "url_postfix", "managed_by"]

    managed_by = serializers.HyperlinkedRelatedField('serviceaccount-detail', read_only=True)
