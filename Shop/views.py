from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    pro = Product.objects.all()
    pal = {'pro' : pro}
    return render(request,'Shop/Home.html', pal)

def about(request):
    return render(request,'Shop/about.html')

def contact(request):
    return render(request,'Shop/contact.html')

def tracker(request):
    return render(request,'Shop/tracker.html')

def search(request):
    return render(request,'Shop/search.html')

def productView(request):
    return render(request,'Shop/productView.html')

def checkout(request):
    return render(request,'Shop/checkout.html')