from math import prod
from django.shortcuts import render  # type: ignore
from .models import Product # Import the Product model
from .forms import ProductForms # Import the ProductForms class
from django.shortcuts import redirect # type: ignore
# Create your views here.
def home(request):
    prod = Product.objects.all() #fetching all the objects from the Product model
    if request.method == 'POST':
        fm = ProductForms(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect ("Success")
    else:
        fm = ProductForms()
    return render(request, 'Electronics/home.html', {'prod' : prod, 'fm': fm}) #rendering the home.html template in the Electronics directory
    
    prod = Product.objects.all()
    fm = ProductForms() #fetching all the objects from the Product model
    return render(request, 'Electronics/home.html', {'prod':prod, 'fm': fm}) #rendering the home.html template in the Electronics directory
