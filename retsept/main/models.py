from django.db import models

# Create your models here.
class Retsept(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ready_time = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Product(models.Model):
    food = models.ForeignKey(Retsept, on_delete=models.CASCADE)
    name = models.CharField(max_length=400)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Comment(models.Model):
    food = models.ForeignKey(Retsept, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author
    