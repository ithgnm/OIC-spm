from django.urls import path
from .views import *
from product.views import *
from cart.views import *


urlpatterns = [
    # Index
    path('', home_view.as_view(), name='index'),

    # Contact
    path('contact', contact_view.as_view(), name='contact'),

    # Product
    path('<slug:slug>', category_view, name='category'),
    path('product/<int:id>', product_detail, name='product'),

    # Cart
    path('cart', cart_detail, name='cart'),
]