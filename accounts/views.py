from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from accounts.models import Profile
from django.shortcuts import redirect

# Create your views here.

class MyLogin(View):
    def get(self, request):
        return render(request,'accounts/login.html')
    
    def POST(self, request):
         if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password1 = request.POST["passw1"]
            confirmpassword = request.POST["passw2"]

            try:
                user = User.objects.get(username=username)
                messages.error(request, f'{username} already taken')
                return redirect('signup_url')
            except:
                pass

            if(password1 != confirmpassword):
                messages.warning(request, "Passwords does not match")
                return redirect('signup_url')

            user = User.objects.create_user(username=username, password=password1, email=email)
            user.save()
            # profile = Profile(user=user)
            # profile.save()
            messages.success(request, f"Account created successfull for {username}")
            redirect('homepage_url')
   
        
class Register(View):
    def get(self, request):
        return render(request,'accounts/register.html') 
    
    def POST(self, request):
        if request.method=="POST": 
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            password1 = request.POST["password"]
            confirmpassword = request.POST["conformpassword"]
            try:
                user = User.objects.get(email=email)
                messages.error(request, f'{email} already taken')
                return redirect('register_ur')
            except:
                pass
            if(password1 != confirmpassword):
                messages.warning(request, "Passwords does not match")
                return redirect('register_url')
            user = User.objects.create_user(firstname=firstname, lastname=lastname, password=password1, email=email)
            user.save()
            # profile = Profile(user=user)
            # profile.save()
            messages.success(request, f"Account created successfull for ")
            redirect('login_url')
        
   