from django.urls import path
from .views import (
    HomePage,
    ProductsListPage,
    ProductPage,
    Search
)
urlpatterns = [
    path("", HomePage.as_view(), name='homepage_url'),
    path("products/<str:category>", ProductsListPage.as_view(), name='products_list_url'),
    path("product/<int:product_id>",  ProductPage.as_view(), name='product_url'),
    path("search/",Search,name='search_url')
]
