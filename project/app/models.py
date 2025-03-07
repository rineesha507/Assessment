from django.db import models

class User(models.Model):
    name=models.CharField(max_length=10)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ${self.price}"    