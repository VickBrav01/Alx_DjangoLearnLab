from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('post-view',views.PostViewSet )
routers.register('comment-view',views.CommentViewSet )

urlpatterns = [
     path('', include(routers.urls)),
     path('feed/', views.UserFeedView.as_view(), name='user-feed'),
     path('posts/<int:pk>/like/', views.LikedPostView.as_view(), name='like-post'),
     path('posts/<int:pk>/unlike/', views.UnlikePostView.as_view(), name='unlike-post'),
]
