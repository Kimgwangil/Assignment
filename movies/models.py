from django.db import models

# Create your models here.
class Actor(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    movies        = models.ManyToManyField('Movies', through='ActorMovie', related_name='movies')

    class Meta:
        db_table = 'actors'


class Movie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()

    class Meta:
        db_table = 'movies'


class ActorMovie(models.Model):
    actors = models.ForeignKey('Actor', on_delete=models.CASCADE)
    movies = models.ForeignKey('Movie', on_delete=models.CASCADE)
