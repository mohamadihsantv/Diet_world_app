from django.urls import path
from .views import add_food_item, list_food_items, update_food_item, delete_food_item

urlpatterns = [
    path('add/', add_food_item, name='add_food_item'),
    path('list/', list_food_items, name='list_food_items'),
    path('update/<int:pk>/', update_food_item, name='update_food_item'),
    path('delete/<int:pk>/', delete_food_item, name='delete_food_item'),
]
