from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.forms import modelformset_factory
from .models import Product, Category, Order, OrderItem
from .form import ProductCreateForms, OrderForm


# Class-based generic Product view
class ProductIndex(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Product.objects.all()
        context['catalogs'] = Category.objects.all()
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context

    def add_to_cart(self):
        queryset = Product.objects.get(slug=self.slug_url_kwarg)


def add_order(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        )
    order = Order.objects.create()
    order.product.add(order_item)
    return redirect('products:product-detail', slug=slug)


class ProductCreate(CreateView):
    model = Product
    form_class = ProductCreateForms
    template_name = 'products/create.html'
    # call out form in Product Create View

    # Redirect when it new product created in view
    success_url = reverse_lazy('products:list')

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    fields = ['title', 'description', 'price', 'quality', 'image', 'category']
    success_url = reverse_lazy('products:list')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')


class OrderView(View):
    def get(self, product, *args, **kwargs):
        order = Order.objects.get(product=self.request.user, ordered=False)
        context = {
            'object': order
        }
        return render(self.request, 'orderview/order.html', context)

