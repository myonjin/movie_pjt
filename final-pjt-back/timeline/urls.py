from django.urls import path
from . import views

urlpatterns = [
    path('getlist/<int:user_id>/', views.get_list)
]
