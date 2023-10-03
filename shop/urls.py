from django.urls import path
from . import views

urlpatterns = [
    path('page/<int:page>/', views.pagination, name='pagination'),
    path('about/', views.about_page, name='about'),
    path('product/<int:product_id>/', views.product_page, name='product'),

]

