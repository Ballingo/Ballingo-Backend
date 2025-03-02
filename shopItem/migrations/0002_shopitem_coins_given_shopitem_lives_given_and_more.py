# Generated by Django 5.1.6 on 2025-03-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopItem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopitem',
            name='coins_given',
            field=models.IntegerField(blank=True, default=100, null=True),
        ),
        migrations.AddField(
            model_name='shopitem',
            name='lives_given',
            field=models.IntegerField(blank=True, default=2, null=True),
        ),
        migrations.AlterField(
            model_name='shopitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
