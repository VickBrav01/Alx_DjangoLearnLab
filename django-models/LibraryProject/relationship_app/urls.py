from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth import views
from django.contrib.auth.views import LogoutView
from .views import admin_view, librarian_view, member_view
from .views import add_book, edit_book, delete_book

urlpatterns = [
    path("", view=list_books, name="list_books"),
    path("libraries/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path("admin/", admin_view, name="admin_view"),
    path("librarian/", librarian_view, name="librarian_view"),
    path("member/", member_view, name="member_view"),
    path("books/add_book/", add_book, name="add_book"),
    path("books/edit_book/<int:book_id>/", edit_book, name="edit_book"),
    path("books/delete_book/<int:book_id>/", delete_book, name="delete_book"),
]
