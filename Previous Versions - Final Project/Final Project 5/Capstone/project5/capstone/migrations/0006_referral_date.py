# Generated by Django 5.0.2 on 2024-02-15 19:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("capstone", "0005_rename_career_timeline_delete_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="referral",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
