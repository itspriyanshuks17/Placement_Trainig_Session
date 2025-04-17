from django.shortcuts import render
from .models import Product
from .forms import ProductForm

def home(request):
    prod=Product.objects.all() # Fetch all products from the database
    context = {'products': prod} # Create a context dictionary to pass to the template
    fm = ProductForm() # Create an instance of the ProductForm
    return render(request, 'Electronics/home.html', {'prod': prod, 'fm':fm})
