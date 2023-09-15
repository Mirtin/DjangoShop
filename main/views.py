from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import *
from cart.cart import Cart


# Create your views here.


def main(request):
    products = ProductTable.objects.all()
    categories = CategoryTable.objects.values_list('category', flat=True)
    input_bar = ''
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            cat_id = CategoryTable.objects.get(category=request.GET.get('category'))
            products = ProductTable.objects.filter(name__icontains=query, cat_id=cat_id)
            input_bar = query

    context = {
        'products': products,
        'input_bar': input_bar,
        'categories': categories,
        'cart_len': len(Cart(request)),
    }
    return render(request, 'index.html', context)


class ProductPage(View):

    def get(self, request, pk):
        product = get_object_or_404(ProductTable, id=pk)
        context = {
            'product': product,
            'cart_len': len(Cart(request)),
        }
        return render(request, 'product_page.html', context)


@login_required
def rate(request, product_id, rating):
    product = get_object_or_404(ProductTable, id=product_id)
    if RatingTable.objects.filter(prod_id=product_id, user=request.user):
        RatingTable.objects.filter(prod_id=product_id, user=request.user).delete()
    rating = RatingTable(user=request.user, rating=rating, prod_id=product)

    rating.save()
    return redirect(f'product/{product_id}')


def about_page(request):
    return render(request, 'about.html')
