# from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
# from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# class BookList(ListAPIView):
#     serializer_class = BookSerializer
#     queryset = Book.objects.all()
class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = []
    
    def get_queryset(self):
        queryset = Book.objects.all()
        params = self.request.query_params
        # title = self.request.query_params.get('title')
        # author = self.request.query_params.get('author')
        if 'title' in params:
            queryset = queryset.filter(title__icontains='title')
        if 'author' in params:
            queryset = queryset.filter(author__icontains='author')
        return queryset
    
    
    
