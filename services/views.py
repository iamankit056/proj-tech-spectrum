from django.shortcuts import render, HttpResponse
from django.views import View
from .models import (
    Category,
    Product,
    ProductImages,
    ProductDescription
)

# Create your views here.
class HomePage(View):
    def get(self, request):
        categories = Category.objects.all()
        products = Product.objects.all()
        productsImages = [ProductImages.objects.filter(product=product) for product in products]
        context = {
            'categories': categories,
            'products': products,
            'productsImages': productsImages
        }
        return render(request,'services/home.html', context=context)
    

class ProductsListPage(View):
    def get(self, request):
        return render(request,'services/products_list.html')

class ProductPage(View):
    def get(self, request):
        return render(request, 'services/sproduct.html')