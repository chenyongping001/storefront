from typing import Collection
from django.db.models import query
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer, Order, OrderItem, Product, Collection

# Create your views here.


def say_hello(request):
    # queryset = Product.objects.filter(description__isnull=False)
    # queryset = Customer.objects.filter(email__contains='.com')
    # queryset = Collection.objects.filter(feature_product__isnull=True)
    # queryset = Product.objects.filter(inventory__lt=10)
    queryset = OrderItem.objects.filter(product__collection__id=3)
    return render(request, "hello.html", {"name": "mosh", "products": list(queryset)})
