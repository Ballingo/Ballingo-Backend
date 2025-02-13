from django.db import models

class Trade(models.Model): # user fk, isActive bool, in-food Food, out-food Food
    user = models.ForeignKey('user.BallingoUser', on_delete=models.CASCADE, related_name='user') # TO DO: change to player
    isActive = models.BooleanField(default=True)
    in_food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='in_food')
    out_food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name='out_food')
    created_at = models.DateTimeField(auto_now_add=True)
