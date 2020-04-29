from rest_framework import serializers

from . import models


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Server
        fields = ["name", "x", "y", "z", "active", "scheme", "host", "url", "url_postfix"]

