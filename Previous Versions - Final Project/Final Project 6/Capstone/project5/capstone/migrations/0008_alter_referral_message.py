# Generated by Django 5.0.2 on 2024-02-15 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("capstone", "0007_referral_subject_alter_referral_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referral",
            name="message",
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]