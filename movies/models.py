from django.db import models

# Create your models here.

class Actors(models.Model):
    
    id = models.ManyToManyField("Movies")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    
    class Meta:
        db_table = "Actors"

class Movies(models.Model):
    
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = "Movies"





