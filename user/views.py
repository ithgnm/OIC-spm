from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user.models import Customer
from product.models import *
import re

# Create your views here.

class register_view(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        category = Category.objects.filter(active=True)
        content = {'category': category}
        return render(request, 'user/register.html', content)

    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        email = request.POST.get('email')
        is_valid = True
        if not password == confirm_password and password:
            is_valid = False
            message = 'Wrong confirm password!'
        if not re.search(r'^\w+$', username):
            is_valid = False
            message = 'Invalid Username!'
        try: Customer.objects.get(username=username)
        except:
            if is_valid is True:
                Customer.objects.create_user(
                    username, email, password,
                    first_name=first_name,
                    last_name=last_name,
                )
                customer = authenticate(username=username, password=password)
                login(request, customer)
                return HttpResponseRedirect('/')
        else: message = 'Username already exists!'
        category = Category.objects.filter(active=True)
        content = {'category': category, 'message': message}
        return render(request, 'user/register.html', content)

class account_view(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/login')
        category = Category.objects.filter(active=True)
        content = {'category': category}
        return render(request, 'user/account.html', content)


