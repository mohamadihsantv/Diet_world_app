from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomerRegistrationForm
from .models import CustomUser

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'customer'  # Customers can only register themselves
            user.save()
            login(request, user)
            return redirect('dashboard_redirect')
    else:
        form = CustomerRegistrationForm()
    return render(request, 'register.html', {'form': form})

def account_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard_redirect')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def dashboard_redirect(request):
    user = request.user
    if user.role == 'customer':
        return redirect('customer_dashboard')
    elif user.role == 'shop_owner':
        return redirect('shop_owner_dashboard')
    elif user.is_superuser:
        return redirect('/admin/')
    return redirect('login')


def account_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request,'home.html')


from product.models import FoodItem  # Correct import for the FoodItem model
@login_required
def customer_dashboard(request):
    # Retrieve all food items for customers
    food_items = FoodItem.objects.all()
    return render(request, 'customer_dashboard.html', {'food_items': food_items})

@login_required
def shop_owner_dashboard(request):
    # Retrieve all food items for shop owners
    food_items = FoodItem.objects.all()
    return render(request, 'shop_owner_dashboard.html', {'food_items': food_items})

