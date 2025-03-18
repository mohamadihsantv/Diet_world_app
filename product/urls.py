from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_food_item, name='add_food_item'),
    path('list/', views.list_food_items, name='list_food_items'),
    path('update/<int:pk>/', views.update_food_item, name='update_food_item'),
    path('delete/<int:pk>/', views.delete_food_item, name='delete_food_item'),
]