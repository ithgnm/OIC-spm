from django.urls import path
from user.views import *
from product.views import *
from cart.views import *
from customer.views import *


urlpatterns = [
    # Index
    path('', home_view.as_view(), name='index'),

    # Contact
    path('contact', contact_view.as_view(), name='contact'),

    # Product
    path('category/<slug:slug>', category_view, name='category'),
    path('product/<int:id>', product_detail, name='product'),

    # Cart
    path('cart', cart_detail, name='cart'),

    # User
    path('login', login_view.as_view(), name='login'),
    path('register', register_view.as_view(), name='register'),
    path('account', account_view.as_view(), name='account'),
    path('logout', logout_view, name='logout'),
]