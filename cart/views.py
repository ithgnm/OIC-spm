from django.contrib.auth import decorators
from django.shortcuts import render
from product.models import *

# from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

@decorators.login_required(login_url='/login')
def cart_detail(request):
    category = Category.objects.filter(active=True)
    content = {'category': category}
    return render(request, 'homepage/cart.html', content)