from django.urls import path
from .views import (
    ShowUserCartItems,
    AddProductToCart
)

urlpatterns = [
    path('user/<int:user_id>', ShowUserCartItems.as_view(), name='user_cart_url'),
    path('product/<int:product_id>', AddProductToCart.as_view(), name='add_to_cart_url'),
]
