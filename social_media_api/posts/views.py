from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import PostSerializer, CommentSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment, Post
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    # filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    # ordering_fields = ["-created_at", "title"]
    # search_fields = ["title"]
    # filterset_fields = {
    #     "title": ["iexact"],
    #     "author__username": ["icontains"],
    # }

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.filter(
            Q(author=user) | Q(author__followers_set=user)
        ).distinct()

        return post


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ["post"]
    ordering_fields = ["created_at"]
    search_fields = ["content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# class CreateCommentView(CreateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def perform_create(self, serializer):
#         author = self.request.user
#         serializer.save(author=author)


# class DetailCommentView(RetrieveUpdateDestroyAPIView):
#     queryset = Comment.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = CommentSerializer


# class CreatePostView(CreateAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def perform_create(self, serializer):
#         author = self.request.user
#         serializer.save(author=author)


# class DetailPostView(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer
#     filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
#     ordering_fields = ["-created_at", "title"]
#     search_fields = ["title"]
#     filterset_fields = {
#         "title": ["iexact"],
#         "author__username": ["icontains"],
#     }
