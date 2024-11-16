from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.


# model for custom base user

class CustomUserManager(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, email, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, profile_photo, password=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            profile_photo=profile_photo
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# model for custom user
class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    # Create permissions such as can_view, can_create, can_edit, and can_delete within your chosen model.
    class Meta:
        permissions = [
            ("can_view"),
            ("can_create"),
            ("can_edit"),
            ("can_delete"),
        ]
