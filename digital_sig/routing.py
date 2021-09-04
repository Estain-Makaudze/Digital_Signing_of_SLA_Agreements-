"""import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import chat.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "digital_sig.settings")

application = ProtocolTypeRouter({"http": get_asgi_application(),"websocket": AuthMiddlewareStack( URLRouter(chat.routing.websocket_urlpatterns)),})

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat2.routing


application = ProtocolTypeRouter({
	  'websocket':AuthMiddlewareStack(
	  	URLRouter(
	  			chat2.routing.websocket_urlpatterns
	  		)
	  	),

	})


	"""