import json
import math

from django.http import HttpResponse
from django.shortcuts import render

import requests

from cryptography.fernet import Fernet

from django.views.decorators.csrf import csrf_exempt

from config import settings

PER_PAGE = 2

key = bytes(settings.ENCRYPTION_KEY, 'utf-8')
fernet = Fernet(key)


def page(request, page_number):
    skip = PER_PAGE * (page_number - 1)

    products_response = requests.get(f'http://localhost:8080/operations/get_products/{skip}/{PER_PAGE}').json()
    products = products_response["products"]
    count = requests.get('http://localhost:8080/operations/get_pages_count/').json()["count"]
    pagination_length = math.ceil(count/PER_PAGE)
    for product, data in products.items():
        product = data
        if product["discount"] != 0:
            product["calculated_price"] = product["price"] - (product["price"] * product["discount"] / 100)
    context = {"products": products,
               "pagination_length": range(1, pagination_length+1),
               "page_number": page_number,
               }
    return render(request, 'pagination.html', context)


def product_page(request, product_id):
    product = requests.get(f'http://localhost:8080/operations/get_product/{product_id}').json()
    average_rating = requests.get(f'http://localhost:8080/rating/get_average_rating/{product_id}').json()["average_rating"]
    context = {
        "product": product,
        "average_rating": average_rating
    }
    return render(request, 'product_page.html', context)


@csrf_exempt
def add_rating(request, page_number):
    data = request.body.decode()
    user_encode_data = json.dumps(data).encode('utf-8')
    token = fernet.encrypt(user_encode_data).decode()
    response = requests.post(f'http://localhost:8080/rating/add_rating/{token}').json()
    return HttpResponse(str(response))


def about_page(request):
    return render(request, 'about.html')
