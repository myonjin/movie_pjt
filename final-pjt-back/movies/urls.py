from django.urls import path
from . import views


urlpatterns = [
    path('totalmovielist/<str:filter>/',views.total_movie_list),
    path('genremovielist/',views.genre_movie_list)
]
