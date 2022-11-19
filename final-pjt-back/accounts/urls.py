from django.urls import path
from . import views

urlpatterns = [
    path('profile/<str:username>/', views.user_profile),
    path('likemovies/<int:user_id>/', views.user_like_movies),
]
