from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# permission Decorators
# view 함수에 @permission_classes([IsAuthenticated]) 데코레이터 달면
# 따로 인증 과정 필요함 (== 토큰 확인 == headers에 토큰 넣어서 요청보내야함)
from rest_framework.decorators import permission_classes 
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer,ArticleSerializer,CommentSerializer
from .models import Article, Comment
from timeline.models import Timeline
# Create your views here.

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            # 타임라인에 추가
            # 1. 글 생성한 유저
            User_model = get_user_model()
            user = User_model.objects.get(pk=request.user.id)
            # 2. 해당 유저의 팔로워 목록 불러오기
            followers = user.followers.all()
            for follower in followers:
                follower_id = follower.id
                # 3. Timeline 인스턴스 생성
                line = Timeline(
                    follower_id = follower_id,
                    username = user.username,
                    profile_img = user.profile_img_src,
                    what = 'article',
                    content = serializer.data['title'],
                    params = serializer.data['id'],
                    router = 'articledetail',
                    is_checked = False,
                )
                line.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET','POST'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        # comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)  

@api_view(['GET'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    print(article.comment_set.all())
    if request.method == 'DELETE':
        comment.delete()
        comments=article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article, user=request.user)
        # serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['POST'])
def likes(request,article_pk):
    # print(request.user)
    # print(request.user.id)
    article = get_object_or_404(Article, pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        is_liked= False
    else:
        article.like_users.add(request.user)
        is_liked= True
    
    data = {
        'is_liked':is_liked,
        'liked_count':article.like_users.count()

    }
    return JsonResponse(data)