from django.contrib import admin
from django.urls import path
from insta_groceries import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("add_product", views.add_product, name='add_product'),
    path("del_product", views.del_product, name='del_product'),
    path("update_product/<int:product_id>/", views.update_product, name='update_product'),
]
