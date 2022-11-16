from django.db import models

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    adult = models.BooleanField()
    poster_path = models.TextField()
    actor = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

# id,title,adult,actors,overview,popularity,release_date,vote_average,vote_count

