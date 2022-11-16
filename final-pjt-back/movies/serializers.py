from rest_framework import serializers
from .models import Movie

class MovieListSerializer(serializers.ModelSerializer):
    # liked_user_set =
    class Meta:
        model = Movie
        fields = ('id','genre','title','poster_path','popularity','release_date',
                    'vote_average','vote_count')