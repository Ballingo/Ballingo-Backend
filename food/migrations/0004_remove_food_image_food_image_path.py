# Generated by Django 5.1.6 on 2025-02-27 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0003_alter_food_language"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="food",
            name="image",
        ),
        migrations.AddField(
            model_name="food",
            name="image_path",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
