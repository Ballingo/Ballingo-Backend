from django.db import models

class Wardrobe(models.Model):
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE, related_name="wardrobe", null=True, blank=True)
    items = models.ManyToManyField('clothes.Clothes')

    def __str__(self):
        return self.user.username

