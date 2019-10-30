from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.http import HttpResponse

from .models import Product
from .form import ProductNewForms
# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)


# Class-based generic view
class ProductIndex(generic.ListView):
    template_name = 'products/list.html'
    model = Product


class ProductDetail(generic.DetailView):
    template_name = 'products/detail.html'
    context_object_name = 'products'
    queryset = Product.objects.all()


def get_product(request):
    form = ProductNewForms
    context = {'form': form}
    if request.method == 'POST':
        form = ProductNewForms(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'products/list.html', context)
        else:
            print('Error Form Invalid')
    return render(request, 'products/product_create.html', context)


def product_about(request):
    context = {}
    return render(request, 'about.html', context)


def product_contact(request):
    context = {}
    return render(request, 'contact.html', context)