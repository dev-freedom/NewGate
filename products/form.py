from django import forms
from .models import Product, OrderItem
# Product Form


class ProductCreateForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'quality', 'price', 'image', 'category']


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ('product', 'quantity')
