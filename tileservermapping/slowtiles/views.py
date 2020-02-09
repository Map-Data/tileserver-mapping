from django.http import HttpResponse

from tileservermapping.mapping.models import Server
from tileservermapping.slowtiles.models import SlowTiles


def insert_tile(request, z, x, y):
    tile_count = SlowTiles.insert(z, x, y)
    if tile_count < 0:
        return HttpResponse("No server responsible", content_type='text', status=404)
    return HttpResponse("Added: {}/{}/{} Count: {}\n".format(z, x, y, tile_count), content_type='text')


def get_server_list(request, z, x, y):
    server = Server.get_server(z, x, y)
    tiles = SlowTiles.objects.filter(server=server, count__gte=5)
    answer = ""
    for tile in tiles:
        answer += "{}/{}/{}\n".format(tile.z, tile.x, tile.y)
    return HttpResponse(answer, content_type='text')
