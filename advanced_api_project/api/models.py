from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL, related_name="author"
    )

    def __str__(self):
        return self.title
