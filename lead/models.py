from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
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

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="leads")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=6, choices=LEAD_PRIORITY.choices, default=LEAD_PRIORITY.LOW)
    status = models.CharField(max_length=9, choices=STATUS_LEAD.choices, default=STATUS_LEAD.NEW)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("lead:leadDetail", args=[self.id])
     