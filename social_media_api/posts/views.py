from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment, Like
from notifications.models import Notification

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserFeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    

class LikedPostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if Like.objects.filter(post=post, user = user).exists():
            return Response({'message': 'Already liked'}, status=status.HTTP_400_BAD_REQUEST)
        

        Notification.objects.create(recipient=post.author, actor=user, verb='liked you post', target=post)
        return Response({'message': 'Post liked'}, status=status.HTTP_201_CREATED)
    

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.filter(post=post, user=user)
        if not like:
            return Response({'message': 'Not like yet'}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
