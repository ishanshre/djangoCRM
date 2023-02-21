from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

User = get_user_model()


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="clients")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("lead:leadDetail", args=[self.id])
     