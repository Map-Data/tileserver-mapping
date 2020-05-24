from rest_framework import serializers, validators
from . import models


class PlanetDumpSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlanetDump
        fields = ['x', 'y', 'z', 'file']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.PlanetDump.objects.all(),
                fields=['x', 'y', 'z']
            )
        ]

    def validate_file(self, value):
        # TODO Validate that file is actually a pbf file
        return value
