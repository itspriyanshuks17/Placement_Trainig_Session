from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def home(request):
    prod = Product.objects.all()  # Fetch all products
    if request.method == 'POST':
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()  # Save the form data to the database
    else:
        fm = ProductForm()  # Initialize an empty form

    return render(request, 'Electronics/home.html', {'prod': prod, 'fm': fm})

def add_product(request):
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm()
    return render(request, 'Electronics/add_product.html', {'form': fm})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        fm = ProductForm(request.POST, request.FILES, instance=product)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm = ProductForm(instance=product)
    return render(request, 'Electronics/edit_product.html', {'form': fm, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.delete()
        return redirect('home')
    return render(request, 'Electronics/delete_product.html', {'product': product})

def success(request):
    return render(request, 'Electronics/success.html')
