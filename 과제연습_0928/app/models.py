from django.db import models

# Create your models here.
class APP(models.Model):
    work = models.CharField(max_length=10)
    todo = models.TextField()
    