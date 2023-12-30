from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    watchlist = models.ManyToManyField(
        "AuctionListing", blank=True, related_name="userWatchlist"
    )


class Category(models.Model):
    category_name = models.CharField(max_length=64)

    def __str__(self):
        return self.category_name


class Bid(models.Model):
    bid = models.FloatField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="userBid"
    )

    def __str__(self):
        return str(self.bid)


class AuctionListing(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=1000)
    imageurl = models.CharField(max_length=10000)
    price = models.ForeignKey(
        Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bidPrice"
    )
    isActive = models.BooleanField(default=True)
    bidCount = models.IntegerField(default=0)
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="owner"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="category",
    )
    creationDate = models.DateField(default=timezone.now)
    closingDate = models.DateField(blank=True, null=True)
    watchlist = models.ManyToManyField(
        User, blank=True, null=True, related_name="auctionWatchlist"
    )

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="author"
    )
    listing = models.ForeignKey(
        AuctionListing,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="listing",
    )
    message = models.CharField(max_length=1000)
    commentDate = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.author} commented {self.message[:20]} on {self.listing}"
