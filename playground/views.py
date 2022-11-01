from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.core.exceptions import ObjectDoesNotExist


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # x = calculate()
    try:
        product = Product.objects.get(pk=0)
    except ObjectDoesNotExist:
        pass
    product = Product.objects.filter(pk=0).first()
    exists = Product.objects.filter(pk=0).exists()



    return render(request, 'hello.html', {'name': 'Mosh'})
