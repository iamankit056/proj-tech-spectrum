from django.urls import path
from .views import AddProductToCart

urlpatterns = [
    path('<int:product_id>', AddProductToCart.as_view(), name='add_to_cart_url'),
]
