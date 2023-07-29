from django.urls import path
from .views import cart
urlpatterns = [
    path("cart/", cart.as_view(), name='cart_url')
]
