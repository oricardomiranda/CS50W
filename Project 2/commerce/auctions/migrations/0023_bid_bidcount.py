# Generated by Django 4.2.7 on 2023-12-29 16:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0022_rename_is_active_auctionlisting_isactive"),
    ]

    operations = [
        migrations.AddField(
            model_name="bid",
            name="bidCount",
            field=models.IntegerField(default=0),
        ),
    ]