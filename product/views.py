from django.shortcuts import render, redirect
from .forms import FoodItemForm
from .models import FoodItem

def add_food_item(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop_owner_dashboard')
    else:
        form = FoodItemForm()
    return render(request, 'product/add_food_item.html', {'form': form})

def list_food_items(request):
    items = FoodItem.objects.all()
    return render(request, 'product/list_food_items.html', {'items': items})

def update_food_item(request, pk):
    food_item = FoodItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, request.FILES, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('shop_owner_dashboard')
    else:
        form = FoodItemForm(instance=food_item)
    return render(request, 'product/update_food_item.html', {'form': form})

def delete_food_item(request, pk):
    food_item = FoodItem.objects.get(pk=pk)
    if request.method == 'POST':
        food_item.delete()
        return redirect('shop_owner_dashboard')
    return render(request, 'product/delete_food_item.html', {'food_item': food_item})
