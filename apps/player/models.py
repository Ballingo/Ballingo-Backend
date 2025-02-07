from django.db import models
from ..language.models import Language

# Create your models here.

class Player(models.Model):
    inventory = models.JSONField(default=list)
    pets = models.JSONField(default=list)
    language = models.JSONField(default=list)
    actual_language = models.ForeignKey(Language, on_delete=models.CASCADE)
    coins = models.IntegerField(default=200)
    active_trades = models.JSONField(default=list)
    lives_counter = models.IntegerField(default=3)
