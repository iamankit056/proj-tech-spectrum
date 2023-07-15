from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.
class index(View):
    def get(self, request):
        return render(request,'services/home.html')

class products_list(View):
    def get(self, request):
        return render(request,'services/products_list.html')

class sproduct(View):
    def get(self, request):
        return render(request, 'services/sproduct.html')