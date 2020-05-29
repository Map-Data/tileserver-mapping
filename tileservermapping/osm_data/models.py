import posixpath
from typing import *

from django.db import models

from tileservermapping.osm_data.storage import OverwriteStorage


def gen_planet_dump_location(instance, filename) -> str:
    """
    Generate uploaded filename based on coordinates of the instance

    :param PlanetDump instance: Instance of the newly created database object
    :param str filename: Originally uploaded file name
    """
    return f'planet_dumps/{instance.z}_{instance.x}_{instance.y}.pbf'


def gen_sql_dump_location(instance, filename) -> str:
    """
    Generate uploaded filename based on coordinates of the file

    :param SqlDump instance: Instance of the newly created database object
    :param str filename: Originally uploaded file name
    """
    return f'sql_dumps/{instance.z}_{instance.x}_{instance.y}.pg_dump'


class PlanetDump(models.Model):
    """
    Planet dump file encoded in PBF format.
    Each database object is mapped to one file in the file storage and can be used to manage that file.

    One PlanetDump does not always store the whole planet but only a smaller portion
    defined by the `x y` and `z` coordinates.
    """

    x = models.IntegerField(help_text='Slippy map coordinate X')
    y = models.IntegerField(help_text='Slippy map coordinate Y')
    z = models.IntegerField(help_text='Slippy map coordinate Z (zoom)')
    file = models.FileField(upload_to=gen_planet_dump_location, null=True, default=None, storage=OverwriteStorage())

    class Meta:
        unique_together = [['x', 'y', 'z']]

    def __str__(self):
        return f'{self.__class__.__name__} of x:{self.x} y:{self.y} z:{self.z}'


class SqlDump(models.Model):
    """
    PostgreSQL Dump files which hold all the data a Tileserver needs.
    """

    x = models.IntegerField(help_text='Slippy map coordinate X')
    y = models.IntegerField(help_text='Slippy map coordinate Z')
    z = models.IntegerField(help_text='Slippy map coordinate Z')
    file = models.FileField(upload_to=gen_sql_dump_location, null=True, default=None, storage=OverwriteStorage())

    class Meta:
        unique_together = [['x', 'y', 'z']]

    def __str__(self):
        return f'{self.__class__.__name__} of x:{self.x} y:{self.y} z:{self.z}'
