from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from accounts.models import Profile
from django.shortcuts import redirect
from services.models import Category

# Create your views here.

class MyLogin(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request,'accounts/login.html', context=context)
    
    def post(self, request):
         if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is None:
                messages.error(request, "Incorrect Username and Password")
                return redirect('login_url')

            login(request, user)
            messages.success(request, f"Account created successfull for {username}")
            return redirect('homepage_url')
   
        
class Register(View):
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            return None

    def get(self, request):
        context = {
            'firstname': '',
            'lastname': '',
            'username': '',
            'email': '',
            'password': '',
            'confirmPassword': '',
            'categories': Category.objects.all()
        }
        return render(request, 'accounts/register.html', context=context) 
    
    def post(self, request):
        if request.method=="POST": 
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            confirmPassword = request.POST["confirmPassword"]
            user = self.get_user(username)

            if user is not None:
                messages.error(request, f'{username} already taken')
                context = {
                    'firstname': firstname,
                    'lastname': lastname,
                    'username': username,
                    'email': email,
                    'password': password,
                    'confirmPassword': confirmPassword,
                    'categories': Category.objects.all()
                }
                return render(request, 'accounts/register.html', context=context) 
            
            if(password != confirmPassword):
                messages.error(request, "Passwords does not match")
                context = {
                    'firstname': firstname,
                    'lastname': lastname,
                    'username': username,
                    'email': email,
                    'password': password,
                    'confirmPassword': confirmPassword,
                    'categories': Category.objects.all()
                }
                return render(request, 'accounts/register.html', context=context) 
            
            User.objects.create_user(
                first_name=firstname, 
                last_name=lastname, 
                password=password, 
                email=email,
                username=username
            )
            messages.success(request, f"Account created successfull for ")
            return redirect('login_url')
        
   