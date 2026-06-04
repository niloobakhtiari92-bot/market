from django.shortcuts import render

# Create your views here.
def product_list(request):
    return render (request , 'index.html')

def product_detail(request):
    return render (request , 'index.html')