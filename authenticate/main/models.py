from django.db import models

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class League(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.last_name
    

