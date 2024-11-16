from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Create your models here.


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ("Admin", "Admin"),
        ("Librarian", "Librarian"),
        ("Member", "Member"),
    ]
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default="Member")
    user = models.OneToOneField(
        User, related_name="user_profile", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user.username} - {self.role}"


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="libraries")

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library, related_name="librarians", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


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
