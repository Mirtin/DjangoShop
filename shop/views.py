from django.shortcuts import render

import requests


PAGE_SIZE = 1


# Create your views here.

def pagination(request, page):
    end = page * PAGE_SIZE
    start = end - PAGE_SIZE
    print(start, end)
    products = requests.get(f'http://localhost:8080/operations/get_products/{start}/{end}').json()["products"]
    for product in products:
        if product["discount"] != 0:
            product["calculated_price"] = product["price"] - (product["price"] * product["discount"] / 100)
    context = {"products": products,
               "pagination_length": range(1, 6),
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
