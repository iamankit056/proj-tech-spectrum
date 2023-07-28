from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views import View
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from accounts.models import Profile
# from django.shortcuts import redirect

# Create your views here.

class Mylogin(View):
    def get(self, request):
        return render(request,'accounts/login.html')
   
        
class register(View):
    def get(self, request):
        return render(request,'accounts/register.html')
   