from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, ProfileSerializer
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action

# from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status


# from rest_framework.authtoken.models import Token

User = get_user_model()


class RegisterView(CreateAPIView):

    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response(
            {
                "access": access_token,
            }
        )


class LoginView(TokenObtainPairView):
    pass


class ProfileView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    # def get_object(self):
    #     return self.request.user


class FollowUser(ViewSet):
    queryset = User.objects.all()

    @action(detail=True, methods=["put"])
    def follow(self, request, pk=None, *args, **kwargs):
        target_user = get_object_or_404(User, pk=pk)
        current_user = request.user

        if current_user == target_user:
            return Response(
                {"message": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        current_user.following.add(target_user)
        target_user.followers.add(current_user)
        return Response(
            {"message": f"You have followed {target_user.username}"},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["delete"])
    def unfollow(self, request, pk=None, *args, **kwargs):
        target_user = get_object_or_404(User, pk=pk)
        current_user = request.user

        if current_user == target_user:
            return Response(
                {"message": "You cannot unfollow yourself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        current_user.following.remove(target_user)
        target_user.followers.remove(current_user)
        return Response(
            {"message": f"You have unfollowed {target_user.username}"},
            status=status.HTTP_200_OK,
        )
