from django.urls import path
from .views import insert_tile, get_server_list, upload_tile

urlpatterns = [
    path('add/<int:z>/<int:x>/<int:y>', insert_tile, name="insert_tile"),
    path('server_list/<int:z>/<int:x>/<int:y>', get_server_list, name="server_list"),
    path('upload_tile/<int:z>/<int:x>/<int:y>.<slug:format>', upload_tile, name='upload_tile'),
]
