from django.shortcuts import render, redirect, HttpResponse
from django.views import View
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from accounts.models import Profile
# from django.shortcuts import redirect

# Create your views here.

class MyLogin(View):
    def get(self, request):
        return render(request,'accounts/login.html')
    
    def post(self, request):
        redirect('homepage_url')
   
        
class Register(View):
    def get(self, request):
        return render(request,'accounts/register.html')
    
    def post(self, request):
        redirect('login_url')
   