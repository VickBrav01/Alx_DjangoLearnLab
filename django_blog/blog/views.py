# from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
    CreateView,
)
from rest_framework.permissions import IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class HomeView(TemplateView):
    template_name = "blog/base.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "blog/register.html"
    success_url = reverse_lazy("home")


class ProfileView: ...


class PostView(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    authentication_class = [IsAuthenticated]
    template_name = "blog/posts.html"
