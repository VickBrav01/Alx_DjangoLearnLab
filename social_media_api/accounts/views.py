from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, ProfileSerializer
from django.contrib.auth import get_user_model

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

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


class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
