# from channels.generic.websocket import WebsocketConsumer
# from asgiref.sync import async_to_sync
# import json

# class ProductListConsumer(WebsocketConsumer):
#     def connect(self):
#         async_to_sync(self.channel_layer.group_add)(
#                "product_page", self.channel_name)
#         self.accept()
        
#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#                 "product_page", self.channel_name)
    
#     def page_reload(self, event):
#         self.send(text_data=json.dumps({
#             "reload_page" : True
#         }))