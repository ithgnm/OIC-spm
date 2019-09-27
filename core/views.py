from django.shortcuts import render
from django.views import View
from product.models import *
from news.models import *


# Create your views here.

class home_view(View):
    def get(self, request):
        carousel = reversed(Carousel.objects.all().order_by('-pk').reverse()[:3])
        product = reversed(Product.objects.all().reverse()[:4])
        content = {'carousel': carousel, 'product': product}
        return render(request, 'homepage/index.html', content)

def contact_view(request):
    return render(request, 'homepage/contact.html')
