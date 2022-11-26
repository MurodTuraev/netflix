import re
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
from rest_framework import filters

from django.contrib.postgres.search import TrigramSimilarity

# Create your views here.


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['imdb', '-imdb']
    search_fields = ["genre"]


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["user"]
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        queryset = Comment.objects.all()
        query = self.request.query_params.get('search')
        if query is not None:
            queryset = Comment.objects.annotate(
                similarity=TrigramSimilarity('text',query)
            ).filter(similarity__gt = 0.1).order_by('-similarity')
        return queryset


class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['user'] = request.user
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        serializer = Comment.objects.get(pk=pk)
        serializer.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    def get(self, request):
        comment = Comment.objects.filter(user_id=self.request.user)
        serializer = CommentSerializer(comment, many=True)
        return Response(data=serializer.data)

# class SearchComment()