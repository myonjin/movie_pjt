from django.db import models

# Create your models here.
class Quiz(models.Model):
    answer = models.CharField(max_length=100)
    chosung = models.CharField(max_length=100)
    src = models.TextField()