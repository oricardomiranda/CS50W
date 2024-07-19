from django.db import models
from django.contrib.auth.models import AbstractUser

class Hash(models.Model):
    text = models.TextField()
    hash = models.CharField(max_length = 64)
