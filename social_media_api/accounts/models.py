from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    bio = models.TextField(max_length=250, null=True)
    profile_picture = models.ImageField(blank=True, null=True)
    followers = models.ManyToManyField("self", symmetrical=False, blank=True)

    def __str__(self):
        return self.username
