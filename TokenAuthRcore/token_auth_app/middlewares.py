from rest_framework.authtoken.model import Token
from urllib.parse import parse_qc
from channels.db import database_sync_async
from django.contrib.auth.models import AnonymousUser

@database_sync_to_async
def returnUser(token_string):
    try:
        user = Token.objects.get
            (key=token_string).user
    except:
        user = AnonymousUser()
    return user


class TokenAuthMiddlerWare:
    def __init__ (self, app):
        self.app  = app
    
    async def __call__ (self, scope, receive, send):
        query_string = scope["query_string"]
        query_params = query_string.decode()
        query_dict = parse_qs(query_params)
        token = query_dict["token"][0]
        user = await returnUser(token)
        scope["user"] = user
        return await self.app(scope, receive, send)
