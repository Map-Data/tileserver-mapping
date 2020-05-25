import posixpath
from django.db import models

from tileservermapping.osm_data.storage import OverwriteStorage


def generate_file_name(instance, filename):
    """
    Generate uploaded filename based on coordinates of the file

    :param instance: Instance of the newly created database object
    :type instance: PlanetDump
    :param filename: Originally uploaded file name
    :type filename: str
    """
    return posixpath.join('planet_dumps', f'{instance.z}_{instance.x}_{instance.y}.pbf')


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
    file = models.FileField(upload_to=generate_file_name, null=True, default=None, storage=OverwriteStorage())

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['x', 'y', 'z'], name='unique_coordinates')
        ]

    def __str__(self):
        return f'{self.__class__.__name__} of x:{self.x} y:{self.y} z:{self.z}'
