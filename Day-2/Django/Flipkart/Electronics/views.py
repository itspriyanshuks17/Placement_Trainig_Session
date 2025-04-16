from django.shortcuts import render
from .models import Product

def home(request):
    prod=Product.objects.all()
    context = {'products': prod}
    return render(request, 'Electronics/home.html', {'prod': prod})
