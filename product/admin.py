from django.contrib import admin
from .models import FoodItem, Category, Species

admin.site.register(FoodItem)
admin.site.register(Category)
admin.site.register(Species)
