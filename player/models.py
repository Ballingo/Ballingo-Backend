from django.db import models

class Player(models.Model):
    user = models.OneToOneField('user.BallingoUser', on_delete=models.CASCADE, related_name='player_profile')
    inventory = models.OneToOneField('inventory.Inventory', on_delete=models.CASCADE, related_name='inventory_holder')
    languages = models.ManyToManyField('language.Language', related_name='players')
    actualLanguage = models.CharField(
        choices=[
            ('en', 'English'), 
            ('es', 'Spanish'), 
            ('de', 'German'), 
            ('ar', 'Arabic'),
            ('ja', 'Japanese')
        ], 
        max_length=20
    )
    