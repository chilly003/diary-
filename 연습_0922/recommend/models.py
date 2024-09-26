from django.db import models

# Create your models here.
class Report(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=20)
    report = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    add_at = models.DateField(auto_now=True)
    image = models.ImageField(blank=True)
    # preference =
