from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import FoodItemForm
from .models import FoodItem

# ✅ Add food item (already filtered by logged-in user)
@login_required
def add_food_item(request):
    if request.user.role != 'shop_owner':
        return redirect('dashboard_redirect')

    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            food_item = form.save(commit=False)
            food_item.owner = request.user  # ✅ Set the owner to the logged-in user
            food_item.save()
            form.save_m2m()  # ✅ Save ManyToMany relationships
            return redirect('shop_owner_dashboard')
    else:
        form = FoodItemForm()

    return render(request, 'product/add_food_item.html', {'form': form})

import logging
logger = logging.getLogger(__name__)

@login_required
def list_food_items(request):
    logger.debug(f"Logged in user: {request.user} (Role: {request.user.role})")

    if request.user.role != 'shop_owner':
        return redirect('dashboard_redirect')

    items = FoodItem.objects.filter(owner=request.user)
    return render(request, 'product/list_food_items.html', {'items': items})



@login_required
def update_food_item(request, pk):
    # ✅ Allow only if the logged-in user is the owner
    food_item = get_object_or_404(FoodItem, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('shop_owner_dashboard')
    else:
        form = FoodItemForm(instance=food_item)
    
    return render(request, 'product/update_food_item.html', {'form': form})

@login_required
def delete_food_item(request, pk):
    # ✅ Allow only if the logged-in user is the owner
    food_item = get_object_or_404(FoodItem, pk=pk, owner=request.user)
    
    if request.method == 'POST':
        food_item.delete()
        return redirect('shop_owner_dashboard')

    return render(request, 'product/delete_food_item.html', {'food_item': food_item})
