# Generated by Django 5.1.6 on 2025-02-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clothes", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clothes",
            name="style",
        ),
        migrations.AddField(
            model_name="clothes",
            name="image_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
