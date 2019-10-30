from django.db import models


# Create your models here.
class Customer(models.Model):
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    yob = models.DateTimeField("Year of birth")
    gender = models.CharField(max_length=1, choices=GENDER)
