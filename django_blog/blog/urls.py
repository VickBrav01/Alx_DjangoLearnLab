from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeView, RegisterView, PostView


urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("posts/<int:pk>", PostView.as_view(), name="posts"),
    path("posts/new/", PostView.as_view(), name="posts"),
    path("posts/<int:pk>/edit/", PostView.as_view(), name="posts"),
    path("posts/<int:pk>/delete/", PostView.as_view(), name="posts"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
