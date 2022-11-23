from django.db import models
# Create your models here.

class Timeline(models.Model):
    follower_id = models.IntegerField()
    username = models.CharField(max_length=50)
    profile_img = models.TextField()
    what = models.CharField(max_length=50)
    content = models.TextField()
    params = models.IntegerField()
    router = models.CharField(max_length=50)
    is_checked = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)