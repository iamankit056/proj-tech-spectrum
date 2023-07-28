from django.urls import path
from .views import Mylogin
from .views import register

urlpatterns = [
    path("Mylogin", Mylogin.as_view()),
    path("register", register.as_view()),
    
]
