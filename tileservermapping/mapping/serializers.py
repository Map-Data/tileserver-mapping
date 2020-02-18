from dynamic_rest import serializers

from . import models


class ServerSerializer(serializers.DynamicModelSerializer):
    class Meta:
        model = models.Server
        fields = ["name", "x", "y", "z", "active", "scheme", "host", "url", "url_postfix"]

