from django.db import models
from ..user.models import User
from ..food.models import Food

# Create your models here.

class Trade(models.Model):
    is_active = models.BooleanField(default=False)
    in_food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='in_food')
    out_food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='out_food')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
