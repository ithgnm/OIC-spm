from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from core.views import *
from product.models import *

# Create your views here.


class login_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        category = Category.objects.filter(active=True)
        content = {'category': category}
        return render(request, 'user/login.html', content)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        customer = authenticate(username=username, password=password)
        category = Category.objects.filter(active=True)
        if customer is None:
            message = 'Wrong Username or Password!'
            content = {'category': category, 'message': message}
            return render(request, 'user/login.html', content)
        login(request, customer)
        return HttpResponseRedirect('/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
