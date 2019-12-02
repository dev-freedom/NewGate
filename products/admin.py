from django.contrib import admin
from products.models import Product, Category, Order, OrderItem

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Order)
