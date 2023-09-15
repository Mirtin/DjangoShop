from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='/'),
    path('about/', views.about_page, name='/'),
    path('product/<int:pk>/', views.ProductPage.as_view(), name='product'),
    path('rate/<int:product_id>/<int:rating>/', views.rate, name='rate'),
]

