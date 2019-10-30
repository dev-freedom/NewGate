from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse

from .models import Product
from .form import ProductNewForms
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'index.html'

# Class-based generic view
class ProductIndex(generic.ListView):
    template_name = 'products/list.html'
    model = Product


class ProductDetail(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductCreate(generic.CreateView):
    fields = ['title', 'description', 'price']
    template_name = 'products/product_create.html'
    model = Product

def product_about(request):
    context = {}
    return render(request, 'about.html', context)



def product_contact(request):
    context = {}
    return render(request, 'contact.html', context)