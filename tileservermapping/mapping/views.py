from django.http import HttpResponse
from dynamic_rest import viewsets
from django.shortcuts import render
from geojson import Polygon, Feature
import mercantile

from .models import Server
from . import serializers


class ServerViewSet(viewsets.DynamicModelViewSet):
    """
    API endpoint that allows servers to be viewed or edited
    """
    queryset = Server.objects.all()
    serializer_class = serializers.ServerSerializer


def get_server(request, z, x, y, format):
    response = HttpResponse()
    response['X-Accel-Redirect'] = Server.get_redirect_server(int(z), int(x), int(y), format)
    return response


def get_cur_tiles(request):
    extracts = ['extracts/1_0_1.pbf', 'extracts/2_0_0.pbf', 'extracts/6_33_22.pbf', 'extracts/2_1_0.pbf',
                'extracts/2_2_0.pbf', 'extracts/2_2_3.pbf', 'extracts/2_3_0.pbf', 'extracts/2_3_2.pbf',
                'extracts/2_3_3.pbf', 'extracts/3_0_2.pbf', 'extracts/3_0_3.pbf', 'extracts/3_3_3.pbf',
                'extracts/3_4_5.pbf', 'extracts/3_5_2.pbf', 'extracts/3_5_3.pbf', 'extracts/3_5_4.pbf',
                'extracts/3_5_5.pbf', 'extracts/3_6_2.pbf', 'extracts/3_7_2.pbf', 'extracts/3_7_3.pbf',
                'extracts/4_2_4.pbf', 'extracts/4_2_5.pbf', 'extracts/4_2_6.pbf', 'extracts/4_2_7.pbf',
                'extracts/4_3_4.pbf', 'extracts/4_3_5.pbf', 'extracts/4_3_6.pbf', 'extracts/4_3_7.pbf',
                'extracts/4_4_4.pbf', 'extracts/4_4_7.pbf', 'extracts/4_5_4.pbf', 'extracts/4_5_5.pbf',
                'extracts/4_5_6.pbf', 'extracts/4_5_7.pbf', 'extracts/4_6_4.pbf', 'extracts/4_6_5.pbf',
                'extracts/4_7_4.pbf', 'extracts/4_8_4.pbf', 'extracts/4_8_6.pbf', 'extracts/4_8_7.pbf',
                'extracts/4_8_8.pbf', 'extracts/4_8_9.pbf', 'extracts/4_9_4.pbf', 'extracts/4_9_6.pbf',
                'extracts/4_9_7.pbf', 'extracts/4_9_8.pbf', 'extracts/4_9_9.pbf', 'extracts/4_12_6.pbf',
                'extracts/4_12_7.pbf', 'extracts/4_13_6.pbf', 'extracts/4_13_7.pbf', 'extracts/5_8_10.pbf',
                'extracts/5_8_11.pbf', 'extracts/5_8_12.pbf', 'extracts/5_8_13.pbf', 'extracts/5_9_10.pbf',
                'extracts/5_9_11.pbf', 'extracts/5_9_12.pbf', 'extracts/5_9_13.pbf', 'extracts/5_14_10.pbf',
                'extracts/5_14_11.pbf', 'extracts/5_15_10.pbf', 'extracts/5_15_11.pbf', 'extracts/5_18_10.pbf',
                'extracts/5_18_11.pbf', 'extracts/5_19_10.pbf', 'extracts/5_19_11.pbf', 'extracts/6_32_20.pbf',
                'extracts/6_32_21.pbf', 'extracts/6_32_22.pbf', 'extracts/6_32_23.pbf', 'extracts/6_33_20.pbf',
                'extracts/6_33_23.pbf', 'extracts/6_34_20.pbf', 'extracts/6_34_21.pbf', 'extracts/6_34_22.pbf',
                'extracts/6_34_23.pbf', 'extracts/6_35_20.pbf', 'extracts/6_35_21.pbf', 'extracts/6_35_22.pbf',
                'extracts/6_35_23.pbf', 'extracts/7_66_42.pbf', 'extracts/7_66_43.pbf', 'extracts/7_67_42.pbf',
                'extracts/7_67_43.pbf']
    tiles = [tile.split('/')[1].split('.')[0] for tile in extracts]

    info = {"{}_{}_{}".format(s.z, s.x, s.y): {
        'status': "active" if s.active else "passive",
        'name': s.name
    } for s in Server.objects.all()}
    map = []

    geojson = []

    for tile in tiles:
        z, x, y = tile.split('_')
        # add box
        # add label
        # add color
        tile2 = mercantile.bounds(int(x), int(y), int(z))
        #poly = Polygon([[(tile2.north, tile2.west), (tile2.north, tile2.east), (tile2.south, tile2.east),
        #                 (tile2.south, tile2.west)]])
        poly = Polygon([[(tile2.west, tile2.north), (tile2.east, tile2.north), (tile2.east, tile2.south),
                         (tile2.west, tile2.south)]])
        feature = Feature(
            geometry=poly,
            properties={
                "tile": "{tile}".format(tile=tile),
                "current": info.get(tile, {}).get('status', "none"),
                "name": info.get(tile, {}).get('name', ""),
            })
        geojson.append(feature)
    return HttpResponse("cur_tiles={}".format(geojson), content_type="text/javascript")
