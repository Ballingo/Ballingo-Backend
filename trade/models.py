from django.db import models

class Trade(models.Model):
    player = models.ForeignKey("player.Player", on_delete=models.CASCADE, related_name="activeTrades", null=True, blank=True)
    isActive = models.BooleanField(default=True)
    in_food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='in_food')
    out_food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='out_food')
    created_at = models.DateTimeField(auto_now_add=True)
