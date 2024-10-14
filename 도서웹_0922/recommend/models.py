from django.db import models
from django.conf import settings

# Create your models here.
class Report(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    report = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    add_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
    star = models.IntegerField(choices=[(1, '⭐'), (2, '⭐⭐'), 
                                        (3, '⭐⭐⭐'),(4,'⭐⭐⭐⭐'),
                                        (5,'⭐⭐⭐⭐⭐')
                                        ], default=3)


class Comment(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    add_at = models.DateField(auto_now=True)