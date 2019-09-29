from django.contrib import admin
from django.contrib.admin.models import *
from django.contrib.auth.models import *
from .models import Customer

# Register your models here.

class user_admin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'is_staff']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username']

admin.site.register(Customer, user_admin)
admin.site.register(Permission)
admin.site.register(LogEntry)

