from django.db import models
from ..coins_shop.models import CoinsShop
from ..clothes.models import Clothes

# Create your models here.

class ShopItem(models.Model):
    type = models.CharField(choices=[('lives', 'Lives'), ('coins', 'Coins'), ('clothes', 'Clothes')], default="coins", max_length=50)
    quantity = models.IntegerField()
    coins_shop_FK = models.ForeignKey(CoinsShop, on_delete=models.CASCADE)
    clothes_FK = models.ForeignKey(Clothes, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.type
