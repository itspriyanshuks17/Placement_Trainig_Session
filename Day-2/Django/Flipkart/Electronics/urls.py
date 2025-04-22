from django.urls import path
from . import views
from Accounts import views as accounts_views  # Import the home view from Accounts

urlpatterns = [
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Fixed syntax
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('success/', views.success, name='success'),
    path('home/', views.home, name='home'),  # Map the home view to /Electronics/home
]
