from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product
from django.views.generic import ListView
import redis


#here you have to initialize Redis and push here a command 
class ProductListView(ListView):
    context_object_name = 'products_list'
    queryset = Product.objects.all()
    template_name = 'scraping_app/index.html'
    paginate_by = 40

    def post(self, request, *args, **kwargs):
        r = redis.Redis()
        r.lpush('valentino:start_urls','https://www.valentino.com/en-us/men/bags')
        r.lpush('valentino:start_urls','https://www.valentino.com/en-us/men/ready-to-wear')
        return HttpResponseRedirect('/')

