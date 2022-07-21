
from django.db import models
from Airport.models import Airport
from django.utils import timezone





class Flight(models.Model):
    aeroplane = models.CharField(max_length=100)
    departure = models.ForeignKey(Airport, on_delete=models.CASCADE,related_name='departure')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='destination')
    departure_datetime = models.DateTimeField(default=timezone.now)
    arrival_datetime = models.DateTimeField()
    max_passengers = models.PositiveIntegerField()
    price = models.PositiveSmallIntegerField()
    total_duration = models.CharField(max_length=25, default=property)
    
    
    @property
    def duration(self):
        duration_difference = self.arrival_datetime - self.departure_datetime
        hours = (duration_difference.total_seconds()/ 3600)

        return f"{hours}  hours"



    def __str__(self):
      return self.aeroplane



    class Meta:
        ordering = ['aeroplane','departure_datetime']
"""
This decorator calculates the difference 
betwen departure and arrival time
"""

        




# Create your models here.
