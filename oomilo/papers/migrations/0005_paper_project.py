# Generated by Django 5.1.4 on 2024-12-15 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("papers", "0004_project_alter_paper_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="paper",
            name="Project",
            field=models.ManyToManyField(blank=True, to="papers.project"),
        ),
    ]
