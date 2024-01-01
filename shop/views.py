import json
import math

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

import requests
from requests.exceptions import ConnectionError

from cryptography.fernet import Fernet

from django.views.decorators.csrf import csrf_exempt

from config import settings

PER_PAGE = 2

key = bytes(settings.ENCRYPTION_KEY, 'utf-8')
fernet = Fernet(key)


def page(request, page_number):
    skip = PER_PAGE * (page_number - 1)

    try:
        products_response = requests.get(f'http://localhost:8080/operations/get_products/{skip}/{PER_PAGE}').json()
        products = products_response["products"]
        count_response = requests.get('http://localhost:8080/operations/get_pages_count/').json()
        count = count_response["count"]
    except ConnectionError:
        context = {"message": 'Can\'t load resources'}
        return render(request, 'error_page.html', context)

    pagination_length = math.ceil(count / PER_PAGE)
    for product, data in products.items():
        product = data
        if product["discount"] != 0:
            product["calculated_price"] = product["price"] - (product["price"] * product["discount"] / 100)
    context = {"products": products,
               "pagination_length": range(1, pagination_length + 1),
               "page_number": page_number,
               }
    return render(request, 'pagination.html', context)


def product_page(request, product_id):
    product_response = requests.get(f'http://localhost:8080/operations/get_product/{product_id}').json()
    product = product_response
    average_rating_response = requests.get(f'http://localhost:8080/rating/get_average_rating/{product_id}').json()
    average_rating = average_rating_response["average_rating"]

    if product["discount"] != 0:
        product["calculated_price"] = product["price"] - (product["price"] * product["discount"] / 100)

    context = {
        "product": product,
        "average_rating": average_rating
    }
    return render(request, 'product_page.html', context)


@csrf_exempt
@login_required
def add_rating(request, page_number):
    data = request.body.decode()
    user_encode_data = json.dumps(data).encode('utf-8')
    token = fernet.encrypt(user_encode_data).decode()
    response = requests.post(f'http://localhost:8080/rating/add_rating/{token}').json()
    return HttpResponse(str(response))


def about_page(request):
    return render(request, 'about.html')


def error_page(request):
    return render(request, 'error_page.html')
