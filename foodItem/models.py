from django.db import models

class FoodItem(models.Model):
    foodlist = models.ForeignKey('foodList.FoodList', on_delete=models.CASCADE, related_name="food_items")
    food = models.ForeignKey('food.Food', on_delete=models.CASCADE, related_name="food_entries")
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.food.name

