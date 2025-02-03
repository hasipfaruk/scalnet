from django.db import models

class Product(models.Model):
    qr_code = models.CharField(max_length=100, unique=True, verbose_name="QR Code Number",default="default_qr_code")
    name = models.CharField(max_length=255, verbose_name="Product Name")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price",default=0.0)

    def __str__(self):
        return self.name


