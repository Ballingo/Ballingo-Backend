from django.db import models

class GamePack(models.Model): # price, name, description, image, category, items: manytomany(shopItem)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    #image_path = models.CharField(max_length=255, blank=True, null=True)
    rarity = models.CharField(
        choices=[
            ('legendary', 'Legendary'),
            ('epic', 'Epic'),
            ('rare', 'Rare'),
            ('uncommon', 'Uncommon'),
            ('common', 'Common'),
        ],
        default='common'
    )
    items = models.ManyToManyField('shopItem.ShopItem', related_name="game_packs")
