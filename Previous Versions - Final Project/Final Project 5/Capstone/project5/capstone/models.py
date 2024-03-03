from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Contact(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    read = models.BooleanField(default=False)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"On {self.date}, {self.email} has sent the message {self.message}"


class Referral(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=1000, blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"On {self.date}, {self.name} has sent the message {self.subject}: {self.message}"


class Timeline(models.Model):
    year = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=250)

    def __str__(self):
        return f"New event for the year {self.year} with the subject {self.subject}"
