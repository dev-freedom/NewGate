from django import forms
from .models import Product
# Product Form


class ProductForms(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    # def save(self, commit=True):
    #     product = super(ProductForms, self).save(commit)
    #     product.save()
    #     return product
