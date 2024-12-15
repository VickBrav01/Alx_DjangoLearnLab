from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User

from rest_framework.authtoken.models import Token


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "bio",
            "profile_picture",
            "followers",
            "following",
        ]

    def create(self, validated_data):

        profile_picture = validated_data.pop("profile_picture", None)
        bio = validated_data.pop("bio", None)

        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            profile_picture=profile_picture,
            bio=bio,
        )

        return user

    def validate_username(self, value):
        if len(value) < 5:
            raise ValidationError("User must be five plus characters")

        return value


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "bio",
            "profile_picture",
            "followers",
            "following",
        ]


# class LoginSerializer(ModelSerializer):
#     username = serializers.CharField()
#     email = serializers.CharField()


# class RegisterSerializer(ModelSerializer):
#     serializer_class = RegisterSerializer
#     Token.objects.create()

#     def create_user(self, validated_data):
#         User = get_user_model().objects.create_user(
#             username=validated_data["username"],
#             email=validated_data["email"],
#             password=validated_data["password"],
#         )
#         return User
