from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Library, Librarian, Book, Author


# Create your views here.


def list_books(request):
    books = Book.objects.all()
    response = (
        "This view should render a simple text list of book titles and their authors."
    )
    for book in books:
        response += f"<li>{book.title} by {book.author.name}</li>"
    response += "</ul>"
    return render(response, "list_books.html", {"name": "name"})


class SpecificLibraryView(ListView):
    model = Library
    template_name = ""
    context_object_name = "library"
    success_url = reverse_lazy("home")

    def get_queryset(self, name):
        library = super().get_queryset()
        specific_library = library.filter(name=name)
        return specific_library
