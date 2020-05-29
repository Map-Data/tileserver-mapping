from rest_framework import serializers, validators
from . import models


class PlanetDumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PlanetDump
        fields = ['url', 'id', 'x', 'y', 'z', 'file']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.PlanetDump.objects.all(),
                fields=['x', 'y', 'z']
            )
        ]

    # TODO: Validate uploaded pbf file


class SqlDumpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.SqlDump
        fields = ['url', 'id', 'x', 'y', 'z', 'file']
        validators = [
            validators.UniqueTogetherValidator(
                queryset=models.SqlDump.objects.all(),
                fields=['x', 'y', 'z']
            )
        ]

    # TODO: Validate uploaded postgresql-dump file
