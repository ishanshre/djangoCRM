from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(_("email address"),unique=True, max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

