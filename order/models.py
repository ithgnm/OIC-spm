from django.db import models
from cart.models import Cart

# Create your models here.

payment_methods = ((0, 'Cash'), (1, 'Visa | Mastercard'), (2, 'Digital Wallet'))

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    payment_type = models.IntegerField(choices=payment_methods, default=0)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    is_completed = models.BooleanField(default=False)