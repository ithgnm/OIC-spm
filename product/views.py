from django.shortcuts import render
from .models import *
from news.models import Carousel

# Create your views here.

def product_detail(request, id):
    category = Category.objects.filter(active=True)
    product = Product.objects.get(pk=id)
    carousel = Carousel.objects.filter(product=id)[:1]
    related = Product.objects.filter(category=product.category, active=True)
    content = {'product': product, 'related': related, 'carousel': carousel, 'category': category}
    return render(request, 'homepage/product.html', content)

def category_view(request, slug):
    category = Category.objects.filter(active=True)
    slug = Category.objects.get(slug=slug, active=True)
    product = Product.objects.filter(category=slug.id)
    content = {'category': category, 'slug': slug, 'product': product}
    return render(request, 'homepage/category.html', content)