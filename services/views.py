from django.shortcuts import render, HttpResponse
from django.views import View
from .models import (
    Category,
    Product,
    ProductImage,
    ProductDescription
)
from cart.models import Cart

# Create your views here.
def CountItemsInCart(request):
    try: 
        return len(Cart.objects.filter(user=request.user))
    except:
        return None


class HomePage(View):
    def get(self, request):
        categories = Category.objects.all()
        products = []
        for product in Product.objects.all():
            product_images = ProductImage.objects.filter(product=product)
            products.append({
                'id': product.id,
                'name': product.name,
                'discount': product.discount,
                'old_price': product.price,
                'new_price': int(product.price*(100-product.discount)/100),
                'image': product_images[0].image if len(product_images) else None,
                'category':product.category,
            })
        context = {
            'categories': categories,
            'products': products,
            'totalItemsInCart': CountItemsInCart(request)
        }
        return render(request,'services/home.html', context=context)
    

class ProductsListPage(View):
    def get(self, request, category):
        categories = Category.objects.all()
        products = []
        for product in Product.objects.filter(category=category):
            product_images = ProductImage.objects.filter(product=product)
            products.append({
                'id': product.id,
                'name': product.name,
                'discount': product.discount,
                'old_price': product.price,
                'new_price': int(product.price*(100-product.discount)/100),
                'image': product_images[0].image if len(product_images) else None
            })
        context = {
            'categories': categories,
            'products': products,
            'category': category,
            'totalItemsInCart': CountItemsInCart(request)
        }
        return render(request,'services/products.html', context=context)


class ProductPage(View):
    def get_product(self, product_id):
        try:
            return Product.objects.get(id=product_id)
        except:
            return None

    def get(self, request, product_id):
        product = self.get_product(product_id)
        if product is None:
            responce = '<h1>404 Not Found</h1>'
            return HttpResponse(responce, status=404)
        context = {
            'categories': Category.objects.all(),
            'product': {
                'id': product.id,
                'name': product.name,
                'discount': product.discount,
                'old_price': product.price,
                'new_price':int( product.price*(100-product.discount)/100),
                'images': ProductImage.objects.filter(product=product),
                'descriptions': ProductDescription.objects.filter(product=product)
            },
            'totalItemsInCart': CountItemsInCart(request)
        }
        return render(request, 'services/product.html', context=context)

class Cart(View):
    def get(self, request):
        return render(request, 'cart/cart.html')