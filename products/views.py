from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy

from .models import Product
from .form import ProductForms



# Class-based generic Product view
class ProductIndex(generic.ListView):
    model = Product
    template_name = 'products/list.html'

    def get_queryset(self):
        self.product = get_object_or_404(Product, name=self.kwargs['product'])
        return Product.objects.filter(product=self.product)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context


class ProductDetail(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreate(generic.CreateView):
    model = Product
    form_class = ProductForms

    def form_valid(self, form):
        form.save()
        return super(ProductCreate, self).form_valid(form)



# class ProductUpdate(generic.UpdateView):
#     model = Product
#     fields = []


class ProductDelete(generic.DeleteView):
    model = Product
    success_url = reverse_lazy('products-list')

