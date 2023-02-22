from django.db import models
from django.contrib.auth import get_user_model

from django.urls import reverse
# Create your models here.


User = get_user_model()


class Plan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.TextField(null=True, blank=True)
    max_leads = models.PositiveIntegerField()
    max_clients = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name="teams")
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='teams')
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_teams")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("team:teamDetail",args=[self.id])