from django.db import models

# Create your models here.

class CoinsShop(models.Model):
    price = models.FloatField()
    name = models.CharField(max_length=100)
    items = models.JSONField(default=list)

    def __str__(self):
        return self.name
