from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    fieldsets = (
        (None, {
            'fields': ('title', 'price', 'description'),
        }
         ),
    )


# Register your models here.
admin.site.register(Product)

