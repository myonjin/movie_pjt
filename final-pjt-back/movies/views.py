import random
from django.shortcuts import render,get_list_or_404
from .models import Movie
from .serializers import MovieListSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET'])
def total_movie_list(request, filter):
    # 기본 (무작위)
    if filter == 'default':
        movies = random.sample(get_list_or_404(Movie), 20)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 평점순
    if filter == 'vote':
        print('이거')
        movies = Movie.objects.all().order_by('-vote_average')[:20]
        print(movies)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 인기순
    if filter == 'popularity':
        movies = Movie.objects.all().order_by('-popularity')[:20]
        print(movies)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

    # 신작순
    if filter == 'new':
        movies = Movie.objects.all().order_by('-release_date')[:20]
        print(movies)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    
    # 구작순
    if filter == 'old':
        movies = Movie.objects.all().order_by('release_date')[:20]
        print(movies)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def genre_movie_list(request):
    id1 = request.GET.get('id1', 'No')
    id2 = request.GET.get('id2', 'No')
    print(id1, id2)
    return