from scraping_project.celery_app import app
from .models import Product

@app.task
def save_products(items):
    for item in items:
        Product.objects.create(
            category = item['category'],
            price = item['price'],
            title = item['title'],
            colors = item['colors'],
            sizes = item['sizes'],
            images = item['images'],
            description = item['description']
        )