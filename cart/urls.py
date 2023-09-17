from django.urls import path
from .views import (
    ShowUserCartItems,
    AddProductToCart,
    RemoveProductToCart,
    MakeOrder
)

urlpatterns = [
    path('', ShowUserCartItems.as_view(), name='user_cart_url'),
    path('product/<int:product_id>', AddProductToCart.as_view(), name='add_to_cart_url'),
    path('cart/<int:cart_id>/remove', RemoveProductToCart.as_view(), name='remove_cart_item_url'),
    path('api/order', MakeOrder.as_view(), name='make_order_url'),
]
