from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from models import Book
from forms import BookForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

# Create your views here.


# logic for view register


def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Account created successfully!")
            # Redirect to login page after registration
            return redirect("login")
    else:
        form = UserCreationForm()  # Display an empty form for GET requests

    return render(request, "relationship_app/register.html", {"form": form})


# logic view for login

# logic view for logout


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


def LogoutView(request):
    return render(request, "logout.html")


def LoginView(request):
    return render(request, "login.html")


def Register(request):
    return render(request, "register.html")


class CustomLoginView(LoginView):
    template_name = "authentication/login.html"
    redirect_authenticated_user = True


# Logout view


class CustomLogoutView(LogoutView):
    template_name = "authentication/logout.html"


# Registration view


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "authentication/register.html"
    success_url = reverse_lazy("login")


"UserCreationForm()", "relationship_app/register.html"


def list_books(request):
    # list of all book instances
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


def check_role(user, role):
    return (
        user.is_authenticated
        and hasattr(user, "userprofile")
        and user.userprofile.role == role
    )


# Admin view


@user_passes_test(lambda user: check_role(user, "Admin"))
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


# Librarian view


@user_passes_test(lambda user: check_role(user, "Librarian"))
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


# Member view


@user_passes_test(lambda user: check_role(user, "Member"))
def member_view(request):
    return render(request, "relationship_app/member_view.html")


# Add book view
@permission_required("relationship_app.can_add_book", raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/add_book.html", {"form": form})


# Edit book view


@permission_required("relationship_app.can_change_book", raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/edit_book.html", {"form": form})


# Delete book view


@permission_required("relationship_app.can_delete_book", raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/delete_book.html", {"book": book})
