from django.db import models
from product.models import *
from user.models import Customer

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)