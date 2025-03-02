from django.db import models

class GamePack(models.Model): # price, name, description, image, category, items: manytomany(shopItem)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    #image_path = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(
        choices=[
            ('lastOportunity', 'Last Oportunity'),
            ('new', 'New'),
            ('popular', 'Popular')
        ]
    )
    items = models.ManyToManyField('shopItem.ShopItem', related_name="game_packs")
