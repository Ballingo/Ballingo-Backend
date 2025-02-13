from django.db import models

class FoodList(models.Model):
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE, related_name="food_lists", null=True, blank=True)

