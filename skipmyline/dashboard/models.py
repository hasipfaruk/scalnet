# dashboard/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Name of the product
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product
    stock = models.PositiveIntegerField()  # Quantity of the product in stock
    availability = models.CharField(
        max_length=50,
        choices=[('In Stock', 'In Stock'), ('Out of Stock', 'Out of Stock')],
        default='In Stock'
    )  # Product availability status
    qr_code = models.CharField(max_length=255, unique=True)  # Unique QR Code for the product

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Automatically update the availability based on the stock level
        if self.stock <= 0:
            self.availability = 'Out of Stock'
        else:
            self.availability = 'In Stock'
        super().save(*args, **kwargs)
