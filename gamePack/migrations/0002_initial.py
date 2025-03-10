# Generated by Django 5.1.6 on 2025-02-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("gamePack", "0001_initial"),
        ("shopItem", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gamepack",
            name="items",
            field=models.ManyToManyField(
                related_name="game_packs", to="shopItem.shopitem"
            ),
        ),
    ]
