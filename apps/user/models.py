from django.db import models
from ..player.models import Player

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    player_fk = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
