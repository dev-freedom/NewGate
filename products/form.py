from django import forms
from django.core import validators

from .models import Product
# Product Form


class ProductNewForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

