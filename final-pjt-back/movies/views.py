import random
from django.shortcuts import render,get_list_or_404
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def order_by_filter(movies, filter):
    if filter == 'default':
        movies = list(movies)
        if len(movies) >= 20:
            movies = random.sample(movies, 20)
        else:
            pass

    # 평점순
    if filter == 'vote':
        print('이거')
        # movies = Movie.objects.all()
        movies = movies.order_by('-vote_average')
        # if len(movies) >= 20:
        #     movies = movies[:20]


    # 인기순
    if filter == 'popularity':
        # movies = Movie.objects.all()
        movies = movies.order_by('-popularity')[:20]

    # 신작순
    if filter == 'new':
        # movies = Movie.objects.all()
        movies = movies.order_by('-release_date')[:20]

    # 구작순
    if filter == 'old':
        # movies = Movie.objects.all()
        movies = movies.order_by('release_date')[:20]
    
    return movies


@api_view(['GET'])
def total_movie_list(request, filter):
    # print(request.GET.get('genre'))
    movies = Movie.objects.all()
    movies = order_by_filter(movies, filter)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genre_movie_list(request, filter):
    genre_id = request.GET.get('id', '')
    genre_id = list(map(int, genre_id.split(',')))
    movies = Movie.objects.all()
    for genre in genre_id:
        genre = Genre.objects.get(pk=genre)
        movies = movies & genre.movie_set.all()
    movies = order_by_filter(movies, filter)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

# axios({
#     method: 'get',
#     url: 'http',
#     params: {
#         id: "1,2,3,4",
#     }
# })

# 장르 여러개 배열에 담은 다음에 join 으로 id:32,23,13 이런 형태로 보내주기