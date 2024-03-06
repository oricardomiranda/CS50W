from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    pass

class Contact(models.Model):
        email = models.EmailField()
        phone = models.CharField(max_length=20, blank=True, null=True)
        message = models.TextField()
        date = models.DateField(default=timezone.now)

        def __str__(self):
            return f"On {self.date}, {self.email} has sent the message {self.message}"

class Referral(models.Model):
    author = models.CharField(max_length=100)
    message = models.CharField(max_length=1000)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")
    message = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S')} with content {self.message}"

class Career(models.Model):
    year = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=250)

    def __str__(self):
        return f"New event for the year {self.year} with the subject {self.subject}"
