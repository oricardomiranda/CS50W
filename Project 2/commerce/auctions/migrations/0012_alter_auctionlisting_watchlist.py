# Generated by Django 4.2.7 on 2023-12-23 22:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0011_auctionlisting_watchlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auctionlisting",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="listingWatchlist",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]