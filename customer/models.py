from django.db import models

# Create your models here.

class Customer(models.Model):
    display_name = models.CharField(default='', max_length=100)
    username = models.CharField(default='', max_length=100, unique=True, null=False)
    password = models.CharField(default='', max_length=100, null=False)
    phone_number = models.CharField(default='', max_length=15)
    email = models.CharField(default='', max_length=100)
    address = models.CharField(default='', max_length=255)
    date_of_birth = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.username