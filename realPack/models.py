from django.db import models

class RealPack(models.Model): # price, name, description, image, category, items: manytomany(shopItem)
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='realPack/', null=True, blank=True)
    category = models.CharField(
        choices=[
            ('lastOportunity', 'Last Oportunity'),
            ('new', 'New'),
            ('popular', 'Popular')
        ]
    )
    items = models.ManyToManyField('shopItem.ShopItem', related_name="real_packs")