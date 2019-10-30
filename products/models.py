from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail_product', kwargs={'pk': self.pk})
#
# class Cate
