from rest_framework import serializers
from .models import Movie,Genre,Review
from django.contrib.auth import get_user_model
class MovieListSerializer(serializers.ModelSerializer):
    # liked_user_set =
    
    class Meta:
        model = Movie
        fields = ('id','genre','title','poster_path','popularity','release_date',
                    'vote_average','vote_count', 'like_users')
        
class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'profile_img_src')
    user = UserSerializer(read_only=True)        
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)
    

class MovieDetailSerializer(serializers.ModelSerializer):

    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'username', 'profile_img_src')    

    genre = GenreNameSerializer(many=True)
    reviews = ReviewSerializer(serializers.ModelSerializer,many=True)

    user = UserSerializer(read_only=True)
    liked_count = serializers.IntegerField(source="like_users.count",read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

