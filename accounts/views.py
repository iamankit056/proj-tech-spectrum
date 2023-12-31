from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from accounts.models import Profile
from django.shortcuts import redirect
from services.models import Category
from cart.models import Cart
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def CountItemsInCart(user):
    try:
        return len(Cart.objects.filter(user=user))
    except:
        return None
    

class Login(View):
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
        

class Logout(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'redirect'
    def get(self, request):
        logout(request)
        return redirect('homepage_url')


class Profile(LoginRequiredMixin, View):
    login_url = 'login_url'
    redirect_field_name = 'redirect'
    def get_user(self, username):
        try:
            return User.objects.get(username=username)
        except:
            return None
        
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'totalItemsInCart': CountItemsInCart(request.user),
            'user' : request.user,
        }
        return render(request, 'accounts/profile.html', context=context)
    
    def post(self,request):
        categories = Category.objects.all()
        firstname = request.POST["fname"]
        lastname = request.POST["lname"]
        email = request.POST["email"]
        user = self.get_user(request.user.username)
        if user is None:
            messages.error('user does not exist.')
        else:
            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()
        return redirect('profile_url')