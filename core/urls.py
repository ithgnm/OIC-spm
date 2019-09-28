from django.urls import path
from .views import *
from product.views import *


urlpatterns = [
    path('', home_view.as_view(), name='index'),
    path('index', home_view.as_view(), name='index'),
    path('index.html', home_view.as_view(), name='index'),

    path('contact', contact_view.as_view(), name='contact'),

    path('product/<int:id>', product_detail, name='product'),
]