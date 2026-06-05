from django.shortcuts import render , redirect
from .models import Product
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def product_detail(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def about(request):
    return render(request, 'about.html')


def  login_user(request):
    return render(request, 'login.html')

def  logout_user(request):
    logout(request)
    messages.success(request , "با موفقیت خارج شدید")
    return redirect("home")
