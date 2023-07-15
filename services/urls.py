from django.urls import path
from .views import * 
urlpatterns = [
    path("",index.as_view()),
    path("products_list/",products_list.as_view()),
    path("sproduct/", sproduct.as_view()),
]
