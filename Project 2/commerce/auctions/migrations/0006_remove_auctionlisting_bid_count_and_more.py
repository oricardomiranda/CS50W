# Generated by Django 4.2.7 on 2023-12-20 20:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0005_rename_auctionlistings_auctionlisting_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="auctionlisting",
            name="bid_count",
        ),
        migrations.RemoveField(
            model_name="auctionlisting",
            name="bid_history",
        ),
    ]