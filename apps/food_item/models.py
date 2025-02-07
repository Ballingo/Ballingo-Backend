from django.db import models
from ..food.models import Food
from ..food_list.models import FoodList

# Create your models here.

class FoodItem(models.Model):
    quantity = models.IntegerField()
    food_fk = models.ForeignKey(Food, on_delete=models.CASCADE)
    food_list_fk = models.ForeignKey(FoodList, on_delete=models.CASCADE)
