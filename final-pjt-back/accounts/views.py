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
def update_following(request):
    print('유저는??????')
    print(request.user.id)
    User_model = get_user_model()
    me = User_model.objects.get(id=request.user.id)
    # serializer = ArticleSerializer(article, data=request.data)
    #     # 수정은 앞쪽에 인스턴스 들어감 + data=request.data
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data
    
    print(request.data['newFollowing'])

    return