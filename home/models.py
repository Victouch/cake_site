from django.db import models

# Create your models here.
class Products(models.Model):     
    product_name = models.CharField(max_length=500)
    product_image = models.ImageField(upload_to="images")
    product_price = models.IntegerField()