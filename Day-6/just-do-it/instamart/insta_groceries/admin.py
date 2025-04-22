from django.contrib import admin
from django.utils.html import format_html
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'image_display', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category','created_at')

    def image_display(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.image.url))
        else:
            return 'No Image'

    image_display.short_description = 'Image'