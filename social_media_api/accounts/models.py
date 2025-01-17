from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField()
    followers = models.ManyToManyField("self", symmetrical=False, related_name='user_followers')
    following =models.ManyToManyField("self", symmetrical=False, related_name='user_following')

    def __str__(self):
        return self.username