import random
from django.shortcuts import render,get_list_or_404
# from .models import Movie, Genre
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserProfileSerializer, UserLikeMoviesSerializer, MovieListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def user_profile(request, username):
    User_model = get_user_model()
    user = User_model.objects.get(username=username)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def user_like_movies(request, user_id):
    User_model = get_user_model()
    user = User_model.objects.get(id=user_id)
    serialzer = UserLikeMoviesSerializer(user)
    return Response(serialzer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def follow(request):
    User_model = get_user_model()
    me = User_model.objects.get(id=request.user.id)
    you = request.data['user_id']
    if me.following.filter(pk=you).exists():
        me.following.remove(you)
    else:
        me.following.add(you)
    serializer = UserProfileSerializer(me)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_img(request):
    src = request.FILES['img-file']
    User_model = get_user_model()
    me = User_model.objects.get(id=request.user.id)
    me.profile_img_src = src
    me.save()
    context = {
        'src': str(me.profile_img_src)
    }
    return Response(context)

# @api_view(['GET'])
# def get_img(request, user_id):
#     User_model = get_user_model()
#     me = User_model.objects.get(id=request.user.id)
#     src = me.profile_img_src
#     render(request, '')

@api_view(['GET'])
def user_like_movies(request, user_id):
    User_model = get_user_model()
    user = User_model.objects.get(pk=user_id)
    serializer = UserLikeMoviesSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def following_like_movies(request, user_id):
    User_model = get_user_model()
    me = User_model.objects.get(pk=user_id)
    following = list(me.following.all())
    print(following[0].id)
    random.shuffle(following)
    for f_user in following:
        if len(f_user.movie_set.all()) > 0:
            break
    serializer = UserLikeMoviesSerializer(f_user)
    return Response(serializer.data)
