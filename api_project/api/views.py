# from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book
from rest_framework.generics import ListAPIView

# Create your views here.
class BookList(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
    