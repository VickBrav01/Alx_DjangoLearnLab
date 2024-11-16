from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('books/', views.book_list, name='book_list'),
    path('example-form/', views.example_form_view, name='example_form'),
]
