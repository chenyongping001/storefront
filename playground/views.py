
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F


def calculate():
    x = 1
    y = 2
    return x


def say_hello(request):
    # x = calculate()

    queryset = queryset = Product.objects.defer('description')

    return render(request, 'hello.html', {
        'name': 'kelemi',
        'products': list(queryset)
    })
