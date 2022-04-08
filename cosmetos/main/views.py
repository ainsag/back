from django.shortcuts import render
from .models import Products
# Create your views here.

def index(request):
    card = Products.objects.all()
    return render(request, 'main/index.html', {'card': card})

def shop(request):
    return render(request, 'main/shop.html')

def checkout(request):
    return render(request, 'main/checkout.html')

def cart(request):
    return render(request, 'main/cart.html')