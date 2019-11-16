from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/')


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=60, default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'slug': self.slug, 'pk': self.pk})


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter()


class Product(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True)
    brand = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    sku = models.CharField(max_length=50)  # sku is stock-keeping unit
    quality = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    old_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, default=0.00)
    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='images/', default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # objects = ProductManager()

    class Meta:
        ordering = []

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail_product', kwargs={'pk': self.pk, 'slug': self.slug})

    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now
