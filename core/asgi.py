"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# 1️⃣  Configure settings **before** anything else Django‑related is imported
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

# 2️⃣  Build the regular Django ASGI app first
django_asgi_app = get_asgi_application()

# 3️⃣  Now it’s safe to import Channels bits and your routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing      # import AFTER Django is ready
# or: import trips.routing if that’s where websocket_urlpatterns live

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns)
        ),
    }
)


