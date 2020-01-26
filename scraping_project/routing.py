# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.urls import re_path, path
# from scraping_app.consumers import ProductListConsumer

# application = ProtocolTypeRouter({
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             re_path(r'', ProductListConsumer)
#         ])
#     ),
# })