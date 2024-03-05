# Generated by Django 4.2.7 on 2023-12-23 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0007_rename_image_url_auctionlisting_imageurl_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="user",
        ),
        migrations.AddField(
            model_name="auctionlisting",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="owner",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
