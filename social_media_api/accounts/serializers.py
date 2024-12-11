from rest_framework.serializers import ModelSerializer, ValidationError
from .models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_followers(self, value):
        if value:
            raise ValidationError("Must not have any followers")
        return value

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
        fields = "__all__"
