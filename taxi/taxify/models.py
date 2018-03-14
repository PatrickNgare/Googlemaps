from django.db import models

class Location(models.Model):
    name=models.CharField(max_length=60,blank=True) 
    lat=models.FloatField(default=0)
    log=models.FloatField(default=0)
    

class Markers(models.Model):
    name=models.CharField(max_length=60)  
    lat=models.FloatField(default=0)
    log=models.FloatField(default=0)



