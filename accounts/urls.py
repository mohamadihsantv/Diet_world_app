from django.urls import path
from .views import (
    register_customer, 
    account_login, 
    dashboard_redirect, 
    shop_owner_dashboard, 
    account_logout,
    home,
    update_profile
)

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('login/', account_login, name='login'),
    path('dashboard/', dashboard_redirect, name='dashboard_redirect'),
    path('shop-owner/', shop_owner_dashboard, name='shop_owner_dashboard'),
    path('logout/', account_logout, name='logout'),
    path('', home, name='home'),
    path('profile/', update_profile, name='update_profile'),

]