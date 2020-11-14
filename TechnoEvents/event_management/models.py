from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    def __str__(self):
        return self.username






class Events(models.Model):
    eventname = models.CharField(max_length=20)
    date = models.DateTimeField()
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)
    # organiser = models.CharField(max_length=100)
    description = models.TextField(max_length=500)