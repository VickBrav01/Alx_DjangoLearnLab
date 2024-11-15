from django.db import models


# Create your models here.
# Author Model:
# name: CharField.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book Model:
# title: CharField.
# author: ForeignKey to Author.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# Library Model:
# name: CharField.
# books: ManyToManyField to Book.
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


# Librarian Model:
# name: CharField.
# library: OneToOneField to Library.
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name
