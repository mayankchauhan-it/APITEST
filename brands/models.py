from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=20)

class BrandImage(models.Model):
    brand = models.ForeignKey('Brand', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='brand_images/')
