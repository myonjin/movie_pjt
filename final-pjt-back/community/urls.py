from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    path('articles/<int:article_pk>/likes/',views.likes),
    # path('articles/<int:article_pk>/likes/<int:user_id>/',views.likes),
    path('articles/comments/', views.comment_list),
    path('articles/comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
    # # # 필수 작성
    # path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # # # optional UI
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]