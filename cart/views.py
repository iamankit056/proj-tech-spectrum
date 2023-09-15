from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .models import Cart
from services.models import (
    Category,
    Product,
    ProductImage,
    ProductDescription,
)
from .models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def CountItemsInCart(user):
    try:
        return len(Cart.objects.filter(user=user))
    except:
        return None
    

class AddProductToCart(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'login_url'
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
    

class CartProductCounter(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'login_url'
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
        

class ShowUserCartItems(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'login_url'
    def get(self, request):
        cart_items = Cart.objects.filter(user=request.user)
        products = []
        total_price = 0
        total_discount = 0
        for cart_item in cart_items:
            product = Product.objects.get(id=cart_item.product_id)
            total_price += product.price
            total_discount += product.discount
            product_images = ProductImage.objects.filter(product=product)
            products.append(
                {
                    "id": product.id,
                    "name": product.name,
                    "discount": product.discount,
                    "old_price": product.price,
                    "new_price": int(product.price * (100 - product.discount) / 100),
                    "image": product_images[0].image if len(product_images) else None,
                    'desc': ProductDescription.objects.filter(product=product)
                }
            )
        total_discount = total_discount / len(cart_items)
        context = {
            "categories": Category.objects.all(),
            "products": products,
            'total_items': len(products),
            "total_price": total_price,
            "total_discount": total_discount,
            "final_price": float(total_price) * (100-total_discount)/100,
            "totalItemsInCart": CountItemsInCart(request.user),
        }
        return render(request, 'cart/cart.html', context=context)