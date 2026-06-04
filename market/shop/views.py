from django.shortcuts import render 
from .models import Product

# Create your views here.
def product_list(request):
    all_product = Product.objects.all()
    return render (request , 'index.html',{'products':all_product})
   

def product_detail(request):
    all_product = Product.objects.all()
    return render (request , 'index.html',{'products':all_product})
    