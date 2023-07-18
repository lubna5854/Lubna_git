from django.db import models

# Create your models here.
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    
class Team(models.Model):
    tname=models.CharField(max_length=250)
    timg=models.ImageField(upload_to='tpics')
    tdesc=models.TextField()


    
   