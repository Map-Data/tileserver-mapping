from django.db import models
import mercantile


class Server(models.Model):
    z = models.IntegerField(null=False)
    x = models.IntegerField(null=False)
    y = models.IntegerField(null=False)

    active = models.BooleanField(default=False)
    managed_by = models.ForeignKey('service_accounts.ServiceAccount',
                                   on_delete=models.CASCADE, blank=True, null=True, default=None)

    scheme = models.CharField(max_length=10, default='http', null=False)
    host = models.CharField(max_length=80, default='127.0.0.1', null=False)
    url = models.CharField(null=False, max_length=80, default="512/all/{z}/{x}/{y}.{format}")

    name = models.CharField(max_length=80)
    url_postfix = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['z', 'x', 'y']),
            models.Index(fields=['active'])
        ]

    def __str__(self):
        return "<Server {} ({}/{}/{})>".format(self.name, self.z, self.x, self.y)

    def get_redirect(self, z, x, y, format):
        url = self.url.format(z=z, x=x, y=y, format=format)
        return "/forward/{name}/{scheme}/{host}/{url}{postfix}".format(name=self.name, scheme=self.scheme, host=self.host, url=url, postfix=self.url_postfix)

    @staticmethod
    def get_server(z, x, y):
        x1 = x
        y1 = y
        for l in range(z, 0, -1):
            #print(z, l, x1, y1)
            server = Server.objects.filter(active=True, z=l, x=x1, y=y1).first()
            if server:
                # todo: return random one
                return server
            x1, y1, _ = mercantile.parent((x1, y1, l))
        return Server.objects.get(z=0, x=0, y=0)

    @staticmethod
    def get_redirect_server(z, x, y, suffix):
        return Server.get_server(z, x, y).get_redirect(z, x, y, suffix)

