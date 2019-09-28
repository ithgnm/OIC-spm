from django.contrib.auth import *
from django.shortcuts import render
from django.views import View
from core.views import *
from product.models import *

# Create your views here.


class login_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            carousel = reversed(Carousel.objects.all().order_by('-pk').reverse()[:3])
            product = Product.objects.filter(active=True).reverse()[:8]
            category = Category.objects.filter(active=True)
            content = {'carousel': carousel, 'product': product, 'category': category}
            return render(request, 'homepage/index.html', content)
        category = Category.objects.filter(active=True)
        content = {'category': category}
        return render(request, 'user/login.html', content)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        category = Category.objects.filter(active=True)
        customer = authenticate(username=username, password=password)
        if customer is None:
            message = 'Wrong Username or Password!'
            content = {'category': category, 'message': message}
            return render(request, 'user/login.html', content)
        login(request, customer)
        carousel = reversed(Carousel.objects.all().order_by('-pk').reverse()[:3])
        product = Product.objects.filter(active=True).reverse()[:8]
        category = Category.objects.filter(active=True)
        content = {'carousel': carousel, 'product': product, 'category': category}
        return render(request, 'homepage/index.html', content)

def logout_view(request):
    logout(request)
    carousel = reversed(Carousel.objects.all().order_by('-pk').reverse()[:3])
    product = Product.objects.filter(active=True).reverse()[:8]
    category = Category.objects.filter(active=True)
    content = {'carousel': carousel, 'product': product, 'category': category}
    return render(request, 'homepage/index.html', content)
