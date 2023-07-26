from django.contrib import admin
from . models import product

# Register your models here.

@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']