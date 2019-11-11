from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)


class Customer(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)


class Staff(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

