# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
# from .models import Product

# @receiver(post_save, sender=Product)
# def refresh_page(**kwargs):
#     channel_layer = get_channel_layer()

#     async_to_sync(channel_layer.group_send)(
#         "product_page", {
#             "type": "page.reload"
#         })