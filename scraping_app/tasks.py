from scraping_project.celery_app import app
from .models import Product

@app.task
def save_products(items):
    Product.objects.bulk_create(
        [Product(**item) for item in items]
    )