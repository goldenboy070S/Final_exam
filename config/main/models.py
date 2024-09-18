from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='car/')

    def __str__(self):
        return self.model
    