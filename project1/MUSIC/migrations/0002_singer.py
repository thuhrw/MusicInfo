# Generated by Django 5.2.3 on 2025-07-01 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MUSIC", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Singer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField()),
                ("pic_url", models.CharField()),
                ("desc", models.CharField()),
                ("url", models.CharField()),
            ],
        ),
    ]
