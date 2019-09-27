from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view.as_view(), name='index'),
    path('index', home_view.as_view(), name='index'),
    path('index.html', home_view.as_view(), name='index'),

    path('contact', contact_view)
]