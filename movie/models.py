from django.db import models
from django.contrib.auth import get_user_model
# from rest_framework.viewsets import ReadOnlyModelViewSet

# Create your models here.


class Actor(models.Model):
    ERKAK = 'Erkak'
    AYOL = 'Ayol'

    CHOICE = [
        (ERKAK, 'erkak'),
        (AYOL, 'ayol')
    ]
    name = models.CharField(max_length=50, blank=True, null=True)
    birthdate = models.DateField(blank=True)
    gender = models.CharField(max_length=5, blank=True, choices=CHOICE)

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    KOMIK = 'Komik'
    DRAMA = 'Drama'
    DETEKTIV = 'Detektiv'
    JANGARI = 'Jangari'
    CHOICE = [
        (KOMIK, 'komik'),
        (DRAMA, 'drama'),
        (DETEKTIV, 'detektiv'),
        (JANGARI, 'jangari'),
    ]
    name = models.CharField(max_length=50, blank=True, null=True)
    year = models.DateField(blank=True)
    genre = models.CharField(max_length=10, choices=CHOICE)
    imdb = models.IntegerField(null=True, blank=True)
    actor = models.ManyToManyField(Actor)

    def __str__(self) -> str:
        return self.name


User = get_user_model()


class Comment(models.Model):

    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='movie_id')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    text = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self) -> str:
        return self.movie_id
