from django.contrib import admin
from django.contrib.auth.models import *
from .models import Customer

# Register your models here.


admin.site.register(Customer)
admin.site.register(Permission)
