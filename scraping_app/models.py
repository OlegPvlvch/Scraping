from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    colors = models.CharField(max_length=200)
    sizes = models.CharField(max_length=200)
    images = models.CharField(max_length=200)
    description = models.TextField()
