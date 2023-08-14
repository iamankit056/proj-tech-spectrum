from django.urls import path
from .views import (
    ShowUserCartItems,
    AddProductToCart,
    CartProductCounter
)

urlpatterns = [
    path('', ShowUserCartItems.as_view(), name='user_cart_url'),
    path('product/<int:product_id>', AddProductToCart.as_view(), name='add_to_cart_url'),
    path('product/<int:cart_id>/<int:counter>', CartProductCounter.as_view(), name='cart_item_counter_url'),
]
