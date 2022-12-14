from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import MovieListSerializer


class UserLikeMoviesSerializer(serializers.ModelSerializer):
    movie_set = MovieListSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'movie_set', 'profile_img_src')

class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)
    following_count = serializers.IntegerField(source='following.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'profile_img_src', 'profile_msg', 'following', 'followers', 'following_count' ,'followers_count',)

class UserFollowingUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = '__all__'