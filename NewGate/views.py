from django.shortcuts import render
from django.views.generic import View
from products.models import Product


class Index(View):
    def get(self, request):
        queryset = Product.objects.all().filter()[:5]
        context = {
            'queryset': queryset,
        }
        return render(request, 'index.html', context)


class Blog(View):
    def get(self, request):
        queryset = Product.objects.all().filter()[:5]
        context = {
            'queryset': queryset,
        }
        return render(request, 'blog.html', context)



class About(View):
    def get(self, request):
        queryset = Product.objects.all().filter()[:5]
        context = {
            'queryset': queryset,
        }
        return render(request, 'about.html', context)


class Contact(View):
    def get(self, request):
        queryset = Product.objects.all().filter()[:5]
        context = {
            'queryset': queryset,
        }
        return render(request, 'contact.html', context)
