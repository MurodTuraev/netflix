from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('id', 'name', 'birthdate', 'gender')


class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'year', 'genre', 'imdb', 'actor')


class CommentSerializer(serializers.ModelSerializer):
    movie_id = MovieSerializer()
    user = get_user_model()

    class Meta:
        model = Comment
        fields = ('id', 'movie_id', 'user', 'text')
