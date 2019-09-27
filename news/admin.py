from django.contrib import admin
from .models import *

# Register your models here.

class carousel_admin(admin.ModelAdmin):
    readonly_fields = ['image_tag']

admin.site.register(News)
admin.site.register(Advertise)
admin.site.register(Carousel, carousel_admin)
