from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, DeleteView)

from .models import Product
from .form import ProductForms


# Class-based generic Product view
class ProductIndex(ListView):
    model = Product
    template_name = 'products/list.html'



class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    fields = ['title', 'description', 'price', 'published',]
    success_url = reverse_lazy('products:list')



# class ProductUpdate(generic.UpdateView):
#     model = Product
#     fields = []


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('products-list')

