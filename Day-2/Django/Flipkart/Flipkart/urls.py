from django.contrib import admin
from django.urls import path
from Electronics import views
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"), #127-0-0-1:8000
    path("success/", views.success, name="success"),
    path("accounts/", include("Accounts.urls")),
    path("Electronics/", include("Electronics.urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
