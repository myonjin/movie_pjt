import random
from django.shortcuts import render,get_list_or_404
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Review
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MovieListSerializer, MovieDetailSerializer,ReviewSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

def order_by_filter(movies, filter):
    if filter == 'default' or filter == 'random':
        movies = list(movies)
        if len(movies) >= 100:
            movies = random.sample(movies, 100)
        else:
            pass

    # 평점순
    if filter == 'vote':
        print('이거')
        # movies = Movie.objects.all()
        movies = movies.order_by('-vote_average')
        # if len(movies) >= 100:
        #     movies = movies[:100]


    # 인기순
    if filter == 'popularity':
        # movies = Movie.objects.all()
        movies = movies.order_by('-popularity')[:100]

    # 신작순
    if filter == 'new':
        # movies = Movie.objects.all()
        movies = movies.order_by('-release_date')[:100]

    # 구작순
    if filter == 'old':
        # movies = Movie.objects.all()
        movies = movies.order_by('release_date')[:100]
    
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



@api_view(['GET'])
def detail_movie(request, movie_id):
    movies = Movie.objects.get(pk=movie_id)
    serializer = MovieDetailSerializer(movies)
    return Response(serializer.data)

# axios({
#     method: 'get',
#     url: 'http',
#     params: {
#         id: "1,2,3,4",
#     }
# })

# 장르 여러개 배열에 담은 다음에 join 으로 id:32,23,13 이런 형태로 보내주기

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def movie_like(request):
    user_id = request.user.id
    movie = Movie.objects.get(id=request.data['movie_id'])
    if movie.like_users.filter(pk=user_id).exists():
        movie.like_users.remove(user_id)
        is_liked = False
    else:
        movie.like_users.add(user_id)
        is_liked = True
    context = {
        'is_liked': is_liked,
    }
    return Response(context, status=status.HTTP_201_CREATED)

@api_view(['POST','DELETE'])
def review_movie(request,movie_id):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        # review = movie.reviews
        # review = Review.objects.get(user_id=request.user.id)
        # print(review)
        # print(request.data)
        # print(request.user.id)
        # print(movie.title)
        
        # 같은 값이 있다
        if movie.reviews.filter(user=request.user).exists():
            review = movie.reviews.get(user=request.user)
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 같은 값이 없을때   
        else:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(movie=movie, user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review = Review.objects.get(pk=1)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)