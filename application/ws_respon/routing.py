from django.urls import path
from application.ws_respon import consumers

websocket_urlpatterns = [
    path('chat/respon/', consumers.MyConsumer.as_asgi()),
]
