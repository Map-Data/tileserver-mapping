from django.urls import path
from .views import insert_tile, get_server_list

urlpatterns = [
    path('add/<int:z>/<int:x>/<int:y>', insert_tile, name="insert_tile"),
    path('server_list/<int:z>/<int:x>/<int:y>', get_server_list, name="server_list")
]
