from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Product
from .form import ProductForms


# Class-based generic Product view
class ProductIndex(ListView):
    model = Product
    template_name = 'products/list.html'
    queryset = Product.objects.all()

class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCategoriesView(TemplateView):
    template_name = 'products/product.html'


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    # call out form in Product Create View
    fields = ['title', 'description', 'price', 'published', 'image']
    # Redirect when it new product created in view
    success_url = reverse_lazy('products:list')


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = ['title', 'description', 'price', 'published']
    success_url = reverse_lazy('products:list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    fields = ['title', 'description', 'price', 'published']
    success_url = reverse_lazy('products:list')
