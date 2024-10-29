"""
ASGI config for TokenAuthRcore project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TokenAuthRcore.settings')

application = get_asgi_application()
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.urls import path
from token_auth_app.consumers import TokenAuthConsumer
from token_auth_app.middlewares import TokenAuthMiddleWare

application = ProtocolTypeRouter(
    {
        "websocket": TokenAuthMiddleWare(
            AllowedHostsOriginValidator(
                URLRouter(
                [path("", TokenAuthConsumer.as_asgi())]
                )
            )
        )
    }
)
