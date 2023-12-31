# Generated by Django 4.2.7 on 2023-12-26 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0018_bid_delete_bids_alter_auctionlisting_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auctionlisting",
            name="price",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bidPrice",
                to="auctions.bid",
            ),
        ),
    ]
