from django.db import models

class ShopItem(models.Model):
    type = models.CharField(
        choices=[
            ('lives', 'Lives'), 
            ('coins', 'Coins'), 
            ('clothes', 'Clothes')
        ], 
        max_length=20
    )
    quantity = models.IntegerField(default=1)
    clothes = models.ForeignKey("clothes.Clothes", on_delete=models.SET_NULL, null=True, blank=True, related_name="shop_items")

    def __str__(self):
        return self.clothes