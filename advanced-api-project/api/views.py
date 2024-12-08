from django.shortcuts import render
from rest_framework import generics, filters
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework as filters

"""
Implement a set of generic views for the Book model to handle CRUD operations. This includes:
A ListView for retrieving all books.
A DetailView for retrieving a single book by ID.
A CreateView for adding a new book.
An UpdateView for modifying an existing book.
A DeleteView for removing a book.

"""


# A ListView for retrieving all books.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # unauthenticated users can view
    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )  # ordering and search filters
    ordering_fields = [
        "title",
        "publication_year",
    ]  # order by title and publication year
    search_fields = ["title", "author"]  # search by title and author


# A DetailView for retrieving a single book by ID.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # unauthenticated users can view


# A CreateView for adding a new book.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # authenticated users only can create


# An UpdateView for modifying an existing book.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # authenticated users only can update


# A DeleteView for removing a book.
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # authenticated users only can delete
