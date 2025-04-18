from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def home(request):
    fm = ProductForm()  # renamed from 'form' to 'fm' to match template
    prod = Product.objects.all()

    if request.method == "POST":
        fm = ProductForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')  # optional but recommended

    return render(request, 'Electronics/home.html', {'prod': prod, 'fm': fm})

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        fm = ProductForm(request.POST, instance=product)
        if fm.is_valid():
            fm.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        fm = ProductForm(instance=product)  # Pre-fill the form with product details
    return render(request, 'Electronics/edit_product.html', {'form': fm, 'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('home')

def success(request):
    return render(request, 'Electronics/success.html')
