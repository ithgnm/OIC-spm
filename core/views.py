from django.shortcuts import render
from django.views import View
from product.models import *
from news.models import *

# Create your views here.

class home_view(View):
    def get(self, request):
        carousel = reversed(Carousel.objects.all().order_by('-pk').reverse()[:3])
        product = reversed(Product.objects.all().reverse()[:4])
        category = Category.objects.all()
        content = {'carousel': carousel, 'product': product, 'category': category}
        return render(request, 'homepage/index.html', content)

class contact_view(View):
    def get(self, request):
        category = Category.objects.all()
        content = {'category': category}
        return render(request, 'homepage/contact.html', content)
