from django.urls import path
from . import views


urlpatterns = [
    path('totalmovielist',views.total_movie_list)
]
