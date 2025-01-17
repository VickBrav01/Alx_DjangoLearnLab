from django.urls import path, include
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('profile/', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('accounts/profile', TemplateView.as_view(template_name='accounts/profile.html'), name='profile'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('update/', views.user_update, name='update'),
    path('posts/', views.Home.as_view(), name='posts'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # path urls for CRUD actions on posts
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/list-view/', views.PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/detail/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # path urls for CRUD actions on comments
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment-create'),
    path('post/comment-list-view/', views.CommentListView.as_view(), name='comment-list'),
    # path('post/<int:pk>/comment-detail/', views.CommentDetailView.as_view(), name='post-comment-detail'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='post-comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='post-comment-delete'),

    # path urls to filter posts by tags
    path('tag/<str:tag_name>/', views.post_by_tag, name='post-by-tag'),
    path('tags/<slug:tag_slug>/', views.PostByTagListView.as_view(), name='posts-by-tag'),

]
