from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def user_directory_path(instance, filename):
    username = instance.username
    return f'users/{username}/{filename}'

class User(AbstractUser):
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_img_src = models.ImageField(upload_to=user_directory_path, blank=True)
    profile_msg = models.TextField(max_length=500, blank=True)
    # birth_date = models.DateField(null=True, blank=True)