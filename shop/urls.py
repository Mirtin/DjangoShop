from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:page_number>/', views.page, name='page'),
    path('about/', views.about_page, name='about'),
    path('product/<int:product_id>/', views.product_page, name='product'),
    path('product/<int:page_number>/add_rating/', views.add_rating, name='add_rating'),
]

