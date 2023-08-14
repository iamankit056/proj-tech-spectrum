from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Cart
from services.models import (
    Category,
    Product
)

# Create your views here.
class AddProductToCart(View):
    def get_product(self, product_id):
        try: 
            return Product.objects.get(id=product_id)
        except:
            return None
        
    def get_cart_item(self, product):
        try: 
            return Product.objects.get(product=product)
        except:
            return None
        
    def get(self, request, product_id):
        product = self.get_product(product_id=product_id)
        if product is None:
            response = '<h1>404 Not Found</h1>'
            return HttpResponse(response, status=404)
        cart_item = self.get_cart_item(product)
        if cart_item is None:
            Cart.objects.create(user=request.user, product=product)
        else:
            cart_item.quentity += 1
            cart_item.save()
        return redirect('product_url', product_id)
    

class ShowUserCartItems(View):
    def get(self, request):
        context = {
            "categories": Category.objects.all(),
        }
        return render(request, 'cart/cart.html', context=context)