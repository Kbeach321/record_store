########## Imports #######################
from django.db import models
from django.contrib.auth.models import AbstractUser

################# Classes #################

class User(AbstractUser):
    pass

class Band(models.Model):
    date_formed = models.IntegerField()
    city_origin = models.CharField(30)
    genre = models.CharField(30)
    band_name = models.CharField(30)
############ FK ############
    creator = band = models.ForeignKey(User, on_delete=models.CASCADE)

class Album(models.Model)
    release_date = models.IntegerField()
    title = models.CharField(30)
    tracks = models.TextField()
    genre = models.CharField(30)
    notes = models.TextField()
################ FK ############
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
