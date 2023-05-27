from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from main.models import ProductTable
from .cart import Cart


# Create your views here.


@login_required
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductTable, id=product_id)
    cart.add(product=product)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ProductTable, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {
        'cart': cart,
        'cart_len': len(cart),
        'total_price': cart.get_total_price(),
    }
    return render(request, 'detail.html', context)
