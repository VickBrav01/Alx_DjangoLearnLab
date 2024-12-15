from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Comment, Post


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post", "author", "content", "created_at", "updated_at"]


class PostSerializer(ModelSerializer):
    comment = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ["title", "author", "content", "comment", "created_at", "updated_at"]
