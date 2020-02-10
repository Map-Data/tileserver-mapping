from pathlib import Path

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

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


def handle_uploaded_file(path, f):
    with open(path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@require_POST
@csrf_exempt
def upload_tile(request, z, x, y, format):
    # TODO auth oth server
    # TODO check if tile in server
    if not SlowTiles.objects.filter(x=x, y=y, z=z, count__gte=5).count():
        return HttpResponse('Tile should not be static\n', content_type="text", status=403)
    path = Path(settings.TILE_WEBSERVER_DIR) / str(z) / str(x)
    if not path.exists():
        path.mkdir(parents=True)
    file = path / "{}.{}".format(y, format)
    existed = file.exists()
    handle_uploaded_file(file, request.FILES['tile'])
    return HttpResponse('Updated\n' if existed else 'OK\n', content_type='text')
