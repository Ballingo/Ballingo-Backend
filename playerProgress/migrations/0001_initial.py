# Generated by Django 5.1.6 on 2025-02-13 21:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("player", "0001_initial"),
        ("questionnaire", "0003_questionnaire_language"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlayerProgress",
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
                ("completed", models.BooleanField(default=False)),
                ("score", models.IntegerField(default=0)),
                ("attempts", models.IntegerField(default=0)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_progress",
                        to="player.player",
                    ),
                ),
                (
                    "questionnaire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="player_progress",
                        to="questionnaire.questionnaire",
                    ),
                ),
            ],
        ),
    ]
