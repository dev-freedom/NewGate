from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/')
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=60, default=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:category', kwargs={'slug': self.slug, 'pk': self.pk})


class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    quality = models.IntegerField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image = models.ImageField(upload_to='images/', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # find the locate to upload images
    # published = models.DateTimeField(timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail_product', kwargs={'pk': self.pk})
    # def save(self):
    #     image = self.image
    #     image.save()
    #     return image
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now





