from django.urls import path
from .views import MyLogin
from .views import Register
from accounts import views

urlpatterns = [
    path("login", MyLogin.as_view(), name='login_url'),
    path("register", Register.as_view(), name='register_url'),
   
    
]
