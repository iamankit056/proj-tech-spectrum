from django.urls import path
from .views import (
    Login,
    Logout,
    Register,
    Profile
)


urlpatterns = [
    path("login", Login.as_view(), name='login_url'),
    path("logout", Logout.as_view(), name='logout_url'),
    path("register", Register.as_view(), name='register_url'),
    path("profile", Profile.as_view(), name='profile_url'),
]
