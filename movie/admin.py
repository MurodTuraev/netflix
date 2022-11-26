from movie.models import Actor, Comment, Movie
from django.contrib import admin

# Register your models here.
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Comment)
