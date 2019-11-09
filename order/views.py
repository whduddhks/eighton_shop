from django.shortcuts import render, redirect
from product.models import Product
from .models import Order


def OrderCreate(request):
    if request.method == 'POST':

        user = request.user
        # 쿼리스트링 pk id 값으로
        get_user = User.objects.get(id=user)

        product = request.POST['product']
        # ?product=pk

        get_product = Product.objects.get(id=product)

        quantity = request.POST.get('quantity')

        order = Order(
            user=get_user,
            product=get_product,
            quantity=quantity
        )
        order.save()
        get_product.stock -= quantity
        get_product.save()

        return


def OrderList(request):
    if request.method == 'GET':
        return
