from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User , on_delete=models.CASCADE, related_name='author_posts')

    tags = TaggableManager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author =models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.ManyToManyField(Post, verbose_name='list of post_tags')

    def __str__(self):
        return self.name
    