from django import forms
from .models import Product
# Product Form

class ProductCreateForms(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title', 'description', 'quality', 'price', 'image', 'category']


