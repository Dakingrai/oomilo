# Generated by Django 5.1.4 on 2024-12-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("papers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
    ]
