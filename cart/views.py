from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Cart
from services.models import (
    Category,
    Product
)
from .models import Cart

# Create your views here.
class AddProductToCart(View):
    def get_product(self, product_id):
        try: 
            return Product.objects.get(id=product_id)
        except:
            return None
        
    def get(self, request, product_id):
        product = self.get_product(product_id=product_id)
        if product is None:
            response = '<h1>404 Not Found</h1>'
            return HttpResponse(response, status=404)
        try:
            Cart.objects.create(user=request.user, product=product)
        except:
            pass
        return redirect('product_url', product_id)
    

class CartProductCounter(View):
    def get_cart_item(self, cart_id):
        try: 
            return Cart.objects.get(id=cart_id)
        except:
            return None
        
    def get(self, request, cart_id, counter):
        cart_item = self.get_cart_item(cart_id=cart_id)
        cart_item.quentity += counter
        cart_item.save()
        return redirect('product_url', cart_item.product.id)
        


class ShowUserCartItems(View):
    def get(self, request):
        context = {
            "categories": Category.objects.all(),
            "cart_items": Cart.objects.filter(user=request.user)
        }
        return render(request, 'cart/cart.html', context=context)