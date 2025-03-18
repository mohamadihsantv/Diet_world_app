from django.urls import path
from django.urls import include, path
from .views import (
    register_customer, 
    account_login, 
    dashboard_redirect, 
    customer_dashboard, 
    shop_owner_dashboard, 
    account_logout,
    home
)

urlpatterns = [
    path('register/', register_customer, name='register_customer'),
    path('login/', account_login, name='login'),
    path('dashboard/', dashboard_redirect, name='dashboard_redirect'),
    path('customer/', customer_dashboard, name='customer_dashboard'),
    path('shop-owner/', shop_owner_dashboard, name='shop_owner_dashboard'),
    path('logout/', account_logout, name='logout'),
    path('', home, name='home'),

]
