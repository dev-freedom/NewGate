from django import forms
from django.core import validators

from .models import Product
# Product Form


class ProductForms(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'price']

