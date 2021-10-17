from django.db import models
from ProfileREST import settings

# Create your models here.

class Profile(models.Model):
    STATUS = [
        ("ACTIVE", "ACTIVE"),
        ("PAUSED", "PAUSED"),
    ]

    name = models.CharField(max_length=20)
    dob = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS, default="ACTIVE")
