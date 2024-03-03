# Generated by Django 4.2.7 on 2023-12-23 22:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0010_alter_auctionlisting_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionlisting",
            name="watchlist",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="user", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
