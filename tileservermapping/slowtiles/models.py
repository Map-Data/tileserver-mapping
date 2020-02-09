from django.db import models, transaction
from tileservermapping.mapping.models import Server


class SlowTiles(models.Model):
    z = models.IntegerField(null=False)
    x = models.IntegerField(null=False)
    y = models.IntegerField(null=False)

    server = models.ForeignKey(Server, on_delete=models.CASCADE)

    count = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['z', 'x', 'y']
        
    def __str__(self):
        return "<SlowTile: {}/{}/{} c: {}>".format(self.z, self.x, self.y, self.count)

    @staticmethod
    def insert(z, x, y):
        """
        inserts a tile z/x/y into the slow tile list, or increase the counter on an existing tile
        :return: the current counter on this tile, or -1 if no tile server is responsible
        """
        server = Server.get_server(z, x, y)
        if server == Server.objects.get(z=0, x=0, y=0):
            # we can not do anything on the external instance
            return -1
        with transaction.atomic():
            try:
                tile = SlowTiles.objects.get(z=z, x=x, y=y)
                tile.count += 1
            except models.ObjectDoesNotExist:
                tile = SlowTiles(z=z, x=x, y=y, server=server)
            tile.save()
        return tile.count
