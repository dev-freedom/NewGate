from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Product
from .form import ProductForms
from .form import ProductForms
# Create your views here.


# Class-based generic Product view
class ProductIndex(generic.ListView):
    model = Product
    template_name = 'products/list.html'


class ProductDetail(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreate(generic.CreateView):
    model = Product
    form_class = ProductForms


class ProductUpdate(generic.UpdateView):
    model = Product
    fields = []


class ProductDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('products-list')

