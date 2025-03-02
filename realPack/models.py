from django.db import models

class RealPack(models.Model): # price, name, description, image, category, items: manytomany(shopItem)
    price = models.FloatField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    image_path = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(
        choices=[
            ('lastOportunity', 'Last Oportunity'),
            ('new', 'New'),
            ('popular', 'Popular')
        ]
    )
    items = models.ManyToManyField('shopItem.ShopItem', related_name="real_packs")