from django.contrib import admin
from .models import *

# Register your models here.

class product_admin(admin.ModelAdmin):
    list_display = ['title', 'price', 'inventory', 'active']
    list_filter = ['active']
    search_fields = ['title']
    readonly_fields = ['image_tag']



admin.site.register(Category)
admin.site.register(Product, product_admin)
admin.site.register(Promotion)