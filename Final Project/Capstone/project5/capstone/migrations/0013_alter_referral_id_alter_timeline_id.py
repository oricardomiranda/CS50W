# Generated by Django 5.0.2 on 2024-02-18 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("capstone", "0012_alter_referral_id_alter_timeline_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referral",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="timeline",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
