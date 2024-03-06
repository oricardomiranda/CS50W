# Generated by Django 4.2.7 on 2023-12-20 20:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        (
            "auctions",
            "0003_alter_auctioncategories_id_alter_auctionlistings_id_and_more",
        ),
    ]

    operations = [
        migrations.RenameModel(
            old_name="AuctionCategories",
            new_name="Categories",
        ),
        migrations.RenameField(
            model_name="categories",
            old_name="category",
            new_name="category_name",
        ),
        migrations.RemoveField(
            model_name="auctionlistings",
            name="item_categories",
        ),
        migrations.RemoveField(
            model_name="auctionlistings",
            name="subtitle",
        ),
        migrations.AddField(
            model_name="auctionlistings",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="category",
                to="auctions.categories",
            ),
        ),
        migrations.AddField(
            model_name="auctionlistings",
            name="creation_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="auctionlistings",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="auctionlistings",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="auctionlistings",
            name="bid_history",
            field=models.ManyToManyField(
                blank=True, related_name="bids_history", to="auctions.bids"
            ),
        ),
        migrations.AlterField(
            model_name="auctionlistings",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="auctionlistings",
            name="image_url",
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name="auctionlistings",
            name="price",
            field=models.FloatField(),
        ),
    ]
