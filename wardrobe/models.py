from django.db import models

class Wardrobe(models.Model):
    user = models.ForeignKey('user.BallingoUser', on_delete=models.CASCADE, related_name="wardrobe_items") # TO DO: Change to Player
    items = models.ManyToManyField('clothes.Clothes')

    def __str__(self):
        return self.user.username

