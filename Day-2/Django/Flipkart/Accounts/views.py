from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required
def home(request):
    return render(request, 'Electronics/home')

@csrf_exempt
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/Electronics/home')
        else:
            return render(request, 'accounts/signin.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')  # Redirect to the signin page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/Signup.html', {'form': form})

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Electronics/home')
    else:
        return render(request, 'accounts/signout.html')
