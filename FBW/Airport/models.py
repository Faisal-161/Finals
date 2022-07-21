from django.db import models
from django.forms import CharField


class Airport(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name



    

# Create your models here.
