import math

from django.shortcuts import render

import requests


PER_PAGE = 2


# Create your views here.

def pagination(request, page):
    skip = PER_PAGE * (page-1)

    products = requests.get(f'http://localhost:8080/operations/get_products/{skip}/{PER_PAGE}').json()["products"]
    count = requests.get('http://localhost:8080/operations/get_pages_count/').json()[0]["count"]
    pagination_length = math.ceil(count/PER_PAGE)
    for product in products:
        if product["discount"] != 0:
            product["calculated_price"] = product["price"] - (product["price"] * product["discount"] / 100)
    context = {"products": products,
               "pagination_length": range(1, pagination_length+1),
               "page": page,
               }
    return render(request, "pagination.html", context)


def product_page(request, product_id):
    product = requests.get(f'http://localhost:8080/operations/get_product/{product_id}').json()["product"][0]
    context = {
        "product": product
    }
    return render(request, "product_page.html", context)


def about_page(request):
    return render(request, "about.html")
