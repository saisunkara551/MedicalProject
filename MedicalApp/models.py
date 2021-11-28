from django.db import models

# Create your models here.
class MedicalData(models.Model):
    sku_id=models.CharField(max_length=50)
    product_id=models.CharField(max_length=50)
    sku_name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    manufacturer_name=models.CharField(max_length=50)
    salt_name=models.CharField(max_length=50)
    drug_form=models.CharField(max_length=50)
    Pack_size=models.CharField(max_length=50)
    strength=models.CharField(max_length=50)
    product_banned_flag=models.CharField(max_length=50)
    unit=models.CharField(max_length=50)
    price_per_unit=models.CharField(max_length=50)
