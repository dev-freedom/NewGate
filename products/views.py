from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)

from .models import Product, Category
from .form import ProductForms


# Class-based generic Product view
class ProductIndex(ListView):
    model = Product
    template_name = 'products/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Product.objects.all()
        return context



class ProductDetail(DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreate(CreateView):
    model = Product
    template_name = 'products/create.html'
    # call out form in Product Create View
    fields = ['title', 'description', 'price', 'quality', 'image', 'category']
    # Redirect when it new product created in view
    success_url = reverse_lazy('products:list')
    #
    # def form_valid(self, form):
    #     product = form.save(commit=False)
    #     product.save()
    #     return self.success_url
    # def post(self, request):
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         return self.form_invalid(form)

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = ['title', 'description', 'price', 'quality', 'image', 'category']
    success_url = reverse_lazy('products:list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    # fields = ['title', 'description', 'price', 'quality', 'image', 'category']
    success_url = reverse_lazy('products:list')


# Class Based View Categories
class CategoriesView(TemplateView):
    model = Category
    template_name = 'products/product.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cate'] = Product.objects.all()[:5]
        return context

