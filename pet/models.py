from django.db import models

class Pet(models.Model):
    # playerId = models.ForeignKey('player.Player', on_delete=models.CASCADE, null=True, blank=True)
    language = models.CharField(
        choices=[
            ('en', 'English'), 
            ('es', 'Spanish'), 
            ('de', 'German'), 
            ('ar', 'Arabic'),
            ('ja', 'Japanese')
        ], 
        max_length=20
    )
    hunger = models.IntegerField(default=100)
    isDead = models.BooleanField()

