from operator import mod
from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length=100)
    ProductCode = models.CharField(max_length=10)
    price = models.IntegerField()
    stock = models.IntegerField()
    describe = models.CharField(max_length=500)
    img = models.CharField(max_length=10000)
class Transaction(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    dateBuy = models.DateTimeField(auto_now_add=True)
    quatily =models.IntegerField(null=True)
    UserName =models.CharField(max_length=200,null=True)
    
    