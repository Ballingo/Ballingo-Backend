from django.db import models

class Inventory(models.Model):
    clothes_inventory = models.OneToOneField('wardrobe.Wardrobe', on_delete=models.CASCADE, related_name='clothes_inventory')
    food_inventory = models.OneToOneField('foodList.FoodList', on_delete=models.CASCADE, related_name='food_inventory')
    coins = models.IntegerField(default=0)
    livesCounter = models.IntegerField(default=0)
