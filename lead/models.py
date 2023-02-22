from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from team.models import Team
# Create your models here.

User = get_user_model()


class Lead(models.Model):
    class LEAD_PRIORITY(models.TextChoices):
        LOW = "LOW", 'Low'
        MEDIUM = "MEDIUM", 'Medium'
        HIGH = "HIGH", 'High'

    class STATUS_LEAD(models.TextChoices):
        NEW = "NEW"
        CONTACTED = "CONTACTED", 'Contacted'
        WON = "WON", 'WON'
        LOST = "LOST", 'Lost'

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="leads")
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=6, choices=LEAD_PRIORITY.choices, default=LEAD_PRIORITY.LOW)
    status = models.CharField(max_length=9, choices=STATUS_LEAD.choices, default=STATUS_LEAD.NEW)
    converted_into_clients = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lead:leadDetail", args=[self.id])


class Comment(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="lead_comments")
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=1000, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="lead_comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"lead comment by {self.created_by.username.title()}"
    