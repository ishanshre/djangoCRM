from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name}"
