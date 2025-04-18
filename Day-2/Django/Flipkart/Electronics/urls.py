from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),  # Fixed syntax
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('success/', views.success, name='success'),
]