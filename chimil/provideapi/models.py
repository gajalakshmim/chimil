from django.db import models
from datetime import date

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)
    floor = models.CharField(max_length=100)
    bname = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    


class Employee(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    empid = models.IntegerField()
    email = models.EmailField(max_length=100)
    startdate = models.DateField(default= date.today)
    lastmodified=models.DateField(default=date.today)
    """LOCATION_CHOICES=(
        ('B','BOSTON'),
        ('N', 'NEWYORK')
        (max_length=19,choices=LOCATION_CHOICES,
                                default='BOSTON')
                                
    )"""

    location = models.ForeignKey(Location, default='1', on_delete=models.SET_DEFAULT)


