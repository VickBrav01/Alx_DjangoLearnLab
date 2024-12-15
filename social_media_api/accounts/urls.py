from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView, FollowUser
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter


router = DefaultRouter()

router.register(r"profile", ProfileView, basename="profile")

parent_router = NestedDefaultRouter(router, r"profile", lookup="profile")
parent_router.register(r"follow", FollowUser, basename="follow")


# from django.

urlpatterns = [
    path("", include(router.urls)),
    path("", include(parent_router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    # path("profile/", ProfileView.as_view(), name="profile"),
]
