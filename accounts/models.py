from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"),unique=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="user/profile/avatar", default="user/profile/default.jpeg")
    bio = models.TextField(max_length=10000, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
