from .models import Library, Librarian, Book, Author


def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books


def list_all_books():
    books = Book.objects.all()
    return books


def get_librarian_by_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.filter(library=library)
    return librarian
