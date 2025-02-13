from django.db import models

class FoodList(models.Model): # user fk, date
    user = models.ForeignKey('user.BallingoUser', on_delete=models.CASCADE, related_name="food_lists") # TO DO: Change to Player

    def __str__(self):
        return self.user.username
