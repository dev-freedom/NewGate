from django import forms
from customers.models import Customer, CustomerInfo

# class CustomerForm


# class CustomerInfoForm
class CustomerInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)

    class Meta:
        model = CustomerInfo
        exclude = ('customer',)