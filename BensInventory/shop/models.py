from django.db import models

class Product(models.Model):
    productname = models.CharField(primary_key=True, max_length=40)
    colour = models.CharField(max_length=20)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    stock = models.IntegerField()
