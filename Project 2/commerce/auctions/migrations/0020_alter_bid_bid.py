# Generated by Django 4.2.7 on 2023-12-26 23:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0019_alter_auctionlisting_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bid",
            name="bid",
            field=models.IntegerField(default=0),
        ),
    ]