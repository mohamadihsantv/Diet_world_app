from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from product.forms import FoodItemForm
from .forms import CustomerRegistrationForm, ProfileForm
from .models import CustomUser
from product.models import FoodItem

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'customer'
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
    return render(request, 'home.html')

@login_required
def shop_owner_dashboard(request):
    # ✅ Show only products owned by the logged-in shop owner
    food_items = FoodItem.objects.filter(owner=request.user).prefetch_related('species')
    return render(request, 'shop_owner_dashboard.html', {'food_items': food_items})

@login_required
def update_food_item(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk, owner=request.user)  # ✅ Ensure ownership

    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.save()
            form.save_m2m()  # ✅ Save many-to-many data
            return redirect('shop_owner_dashboard')
    else:
        form = FoodItemForm(instance=food_item)
        form.fields['species'].initial = food_item.species.all()  # ✅ Pre-populate species data

    return render(request, 'product/update_food_item.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('shop_owner_dashboard' if request.user.role == 'shop_owner' else 'customer_dashboard')
    else:
        form = ProfileForm(instance=request.user, user=request.user)

    return render(request, 'update_profile.html', {'form': form})
