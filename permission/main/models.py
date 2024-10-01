from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name