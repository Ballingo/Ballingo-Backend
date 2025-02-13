from django.db import models

class Pet(models.Model):
    player = models.ForeignKey("player.Player", on_delete=models.CASCADE, related_name="pets", null=True, blank=True)
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

