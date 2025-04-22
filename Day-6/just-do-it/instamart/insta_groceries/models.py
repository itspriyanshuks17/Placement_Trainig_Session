from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField(default=0)  # Assuming stock is already present
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.name
