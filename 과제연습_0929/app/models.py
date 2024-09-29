from django.db import models

# Create your models here.
class APP(models.Model):
    name = models.CharField(max_length=10)
    report = models.TextField()
    image = models.ImageField(blank=True)