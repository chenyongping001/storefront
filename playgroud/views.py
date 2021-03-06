from typing import Collection
from django.db.models import Q, F
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Cart, CartItem, Customer, Order, OrderItem, Product, Collection
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

# Create your views here.


def say_hello(request):
    # queryset = Product.objects.filter(description__isnull=False)
    # queryset = Customer.objects.filter(email__contains='.com')
    # queryset = Collection.objects.filter(feature_product__isnull=True)
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = OrderItem.objects.filter(product__collection__id=3)

    # queryset = Product.objects.filter(inventory__lt=10, unit_price__lt=20)
    # queryset = Product.objects.filter(
    # inventory__lt=10).filter(unit_price__lt=20)

    # queryset = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # queryset = Product.objects.filter(inventory=F('collection__id'))

    # queryset = Product.objects.order_by('unit_price', '-title').reverse()

    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')

    # queryset = Product.objects.filter(unit_price__lt=20)

    # queryset = Product.objects.all()[5:10]

    # queryset = Product.objects.values('id', 'title', 'collection__title')
    # queryset = Product.objects.values_list('id', 'title', 'collection__title')

    # queryset = Product.objects.filter(
    #     id__in=OrderItem.objects.values('product__id').distinct()).order_by('title')

    # queryset = Product.objects.only('id', 'title')

    # queryset = Product.objects.defer('description')

    # queryset = Product.objects.select_related('collection').all()

    # queryset = Product.objects.select_related(
    #     'collection').prefetch_related('promotions').all()

    # queryset = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]

    # return render(request, "hello.html", {"name": "mosh", "orders": list(queryset)})

    # result = Product.objects.aggregate(
    #     count=Count('id'), min_price=Min('unit_price'))

    # result = Order.objects.aggregate(count=Count('id'))

    # result = OrderItem.objects.filter(
    #     product__id=1).aggregate(units_sold=Sum('quantity'))

    # result = Order.objects.filter(customer__id=1).aggregate(count=Count('id'))

    # result = Product.objects.filter(collection__id=3)\
    #     .aggregate(
    #         min_price=Min('unit_price'),
    #         max_price=Max('unit_price'),
    #         avg_price=Avg('unit_price'),
    # )

    # results = Customer.objects.annotate(
    #     last_order_id=Max('order__id')
    # )

    # results = Collection.objects.annotate(
    #     products_count=Count('product')
    # )

    # results = Customer.objects.annotate(
    #     order_count=Count('order')
    # ).filter(
    #     order_count__gt=5
    # )

    # results = Customer.objects.annotate(
    #     total_spent=Sum(
    #         F('order__orderitem__unit_price') *
    #         F('order_orderitem_quantity')
    #     )
    # )

    # results = Product.objects.annotate(
    #     total_sales=Sum(
    #         F('orderitem__quantity') *
    #         F('orderitem__unit_price')
    #     )
    # ).order_by('-total_sales')[:5]

    cart = Cart()
    cart.save()
    cartitem = CartItem()
    cartitem.product_id = 1
    cartitem.quantity = 2
    cartitem.cart = cart
    cartitem.save()

    item1 = CartItem.objects.get(pk=1)
    item1.quantity = 3
    item1.save()

    return render(request, "hello.html", {"name": "mosh", })
