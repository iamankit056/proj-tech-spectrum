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
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
import razorpay

# Create your views here.
def CountItemsInCart(user):
    try:
        return len(Cart.objects.filter(user=user))
    except:
        return None
    

class AddProductToCart(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'redirect'
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


class RemoveProductToCart(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'redirect' 
    def get_cart_item(self, cart_id):
        try: 
            return Cart.objects.get(id=cart_id)
        except:
            return None

    def get(self, request, cart_id):
        cart_item = self.get_cart_item(cart_id)
        if cart_item is not None:
            cart_item.delete()
        return redirect('user_cart_url')
    

class ShowUserCartItems(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'redirect'
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
                    "cart_id": cart_item.id,
                    "id": product.id,
                    "name": product.name,
                    "discount": product.discount,
                    "old_price": product.price,
                    "new_price": int(product.price * (100 - product.discount) / 100),
                    "image": product_images[0].image if len(product_images) else None,
                    'desc': ProductDescription.objects.filter(product=product)
                }
            )
        try:
            total_discount = total_discount / len(cart_items)
        except:
            total_discount = 0
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
    

class MakeOrder(APIView):
    # permission_classes = [IsAuthenticated]
    def post(self, request):
        total_amount = request.data.get('amount')
        total_amount = float(total_amount)
        client = razorpay.Client(auth=("rzp_test_TCjpjFREfXmCLQ", "gmxnPSmihhtG2IAXHGplMQwS"))
        data = { "amount": total_amount*100, "currency": "INR", "receipt": "order_rcptid_11" }
        payment = client.order.create(data=data)
        return Response(data=payment)