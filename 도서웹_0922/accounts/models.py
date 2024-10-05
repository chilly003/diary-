from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Article(models.Model):
    query = models.TextField( null=True, blank=True)
    title = models.TextField()
    link = models.URLField(max_length=500)
