from rest_framework import serializers
from .models import Movie,Genre

class MovieListSerializer(serializers.ModelSerializer):
    # liked_user_set =
    
    class Meta:
        model = Movie
        fields = ('id','genre','title','poster_path','popularity','release_date',
                    'vote_average','vote_count', 'like_users')
        

class MovieDetailSerializer(serializers.ModelSerializer):
    class GenreNameSerializer(serializers.ModelSerializer):
        class Meta:
            model = Genre
            fields = '__all__'

    # liked_user_set =
    class Meta:
        model = Movie
        fields = '__all__'

