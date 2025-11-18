from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('vendor-dashboard/', views.vendor_dashboard, name='vendor_dashboard'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
]
