from django.shortcuts import render
from .models import *
from news.models import Carousel

# Create your views here.

def product_detail(request, id):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    carousel = Carousel.objects.filter(product=id)[:1]
    related = Product.objects.filter(category=product.category)
    content = {'product': product, 'related': related, 'carousel': carousel, 'category': category}
    return render(request, 'homepage/product.html', content)

