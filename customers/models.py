from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    yob = models.DateTimeField("Year of birth")
    gender = models.CharField(max_length=1, choices=GENDER)

    def __str__(self):
        return self.first_name


class CustomerInfo(models.Model):
    # Create relationship (don't inherit from User!
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio = models.URLField(blank=True)
    profile = models.ImageField(upload_to='profile_pics')

    def __str__(self):
        return self.customer.username
