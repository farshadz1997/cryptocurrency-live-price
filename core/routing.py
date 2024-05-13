from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import os
import coins.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

django_application = get_asgi_application()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
            coins.routing.websocket_urlpatterns
        )
})