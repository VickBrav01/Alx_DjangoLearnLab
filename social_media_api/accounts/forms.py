from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"

        help_text = {
            "username": "This will be your username",
        }
