from django.urls import path
from . import views


urlpatterns = [
    path('totalmovielist/<str:filter>/',views.total_movie_list),
    path('genremovielist/<str:filter>/',views.genre_movie_list),
    path('detail/<int:movie_id>/',views.detail_movie),
    path('like/',views.movie_like),
    path('detail/<int:movie_id>/review/',views.review_movie),
    path('userreviewmovielist/<int:user_id>/<int:score>/', views.review_list),
]
