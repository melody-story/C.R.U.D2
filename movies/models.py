from django.db import models

# Create your models here.

class Actors(models.Model):                          # 중간 테이블 있는 경우 
    Movies        = models.ManyToManyField("Movies") #, through="Actors_Movies")
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    
    class Meta:
        db_table = "Actors"

class Movies(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = "Movies"

# 중간테이블 형성
# 
# class Actors_Movies():
#     actor = models.ForeignKey("Actors", on_delete=models.CASCADE)
#     movie = models.ForeignKey("Movies", on_delete=models.CASCADE)

#     class Meta:
#         db_table = "Actors_Movies"





