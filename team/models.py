from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_teams")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
