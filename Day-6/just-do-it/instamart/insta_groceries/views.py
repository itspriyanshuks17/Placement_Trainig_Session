from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


def home(request):
    query = request.GET.get('q', '')
    if query:
        prods = Product.objects.filter(name__icontains=query) | Product.objects.filter(category__icontains=query)
    else:
        prods = Product.objects.all().order_by('-created_at')  # Order by creation date (descending)
    form = ProductForm()
    return render(request, 'insta_groceries/home.html', {'form': form, 'prods': prods, 'query': query})

def about(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ProductForm()
    return render(request, 'insta_groceries/about.html', {'form': form})


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_product')
    else:
        form = ProductForm()
    return render(request, 'insta_groceries/add_product.html', {'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('update_product', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'insta_groceries/update_product.html', {'form': form, 'product': product})

def del_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        if product_id:  # Check if product_id is not empty
            try:
                product = get_object_or_404(Product, id=int(product_id))
                product.delete()
                return redirect('del_product')
            except ValueError:
                # Handle the case where product_id is not a valid integer
                return render(request, 'insta_groceries/del_product.html', {
                    'products': Product.objects.all(),
                    'error': 'Invalid Product ID. Please enter a valid number.'
                })
        else:
            # Handle the case where product_id is empty
            return render(request, 'insta_groceries/del_product.html', {
                'products': Product.objects.all(),
                'error': 'Product ID cannot be empty.'
            })
    return render(request, 'insta_groceries/del_product.html', {
        'products': Product.objects.all()
    })
