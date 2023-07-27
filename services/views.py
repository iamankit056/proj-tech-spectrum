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
        products = []
        for product in Product.objects.all():
            product_images = ProductImages.objects.filter(product=product)
            products.append({
                'id': product.id,
                'name': product.name,
                'discount': product.discount,
                'old_price': product.price,
                'new_price': product.price*(100-product.discount)/100,
                'image': product_images[0].image if len(product_images) else None
            })

        context = {
            'categories': categories,
            'products': products,
        }
        return render(request,'services/home.html', context=context)
    

class ProductsListPage(View):
    def get(self, request, category):
        return render(request,'services/products_list.html')

class ProductPage(View):
    def get(self, request, product_id):
        return render(request, 'services/sproduct.html')