from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import product

def home(request):
    return render(request, "app/home.html")

class CategoryView(View):
    def get(self, request, val):
        products = product.objects.filter(category=val)
        title = product.objects.filter(category=val).values('title')
        return render(request, "app/category.html", locals())
