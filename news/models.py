from django.db import models
from django.utils import safestring
from django.conf import settings
from product.models import Product

# Create your models here.


class News(models.Model):
    title = models.CharField(default='', max_length=100)
    subtitle = models.CharField(default='', max_length=255)
    topic = models.CharField(default='', max_length=100)
    image = models.CharField(max_length=255, default='')
    author = models.CharField(default='', max_length=100)
    content = models.TextField(default='')

    def __str__(self):
        return self.title

class Advertise(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.CharField(max_length=100, default='')
    description = models.TextField(default='')

    def __str__(self):
        return self.title

class Carousel(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='images/carousel/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return safestring.mark_safe(
                '<img src="%s%s" width="150" height="150" />' % (settings.MEDIA_URL, self.image))
        else:
            return ""

    image_tag.short_description = 'image'
    image_tag.allow_tags = True