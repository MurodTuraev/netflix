from rest_framework.authtoken import views
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

actor = DefaultRouter()
actor.register("actor", ActorViewSet, 'api')
actor.register("movie", MovieViewSet, 'api')
actor.register("comment", CommentViewSet, 'api')

urlpatterns = [
    path("", include(actor.urls)),
    path('comments/', CommentAPIView.as_view())
]   

urlpatterns += [
    path('api/auth/', views.obtain_auth_token)
]
