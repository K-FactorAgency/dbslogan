from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    content = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    likes = models.ManyToManyField(User, blank=True, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
