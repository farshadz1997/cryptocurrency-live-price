from .consumers import CoinsListConsumer
from django.urls import path


websocket_urlpatterns =[
    path("ws/coins", CoinsListConsumer.as_asgi()),
]