from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

from .models import Product
# Product Form


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

