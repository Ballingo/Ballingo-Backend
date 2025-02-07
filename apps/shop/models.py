from django.db import models

# Create your models here.

class Shop(models.Model):
    realMoneyPacks = models.JSONField(default=list)
    clothesPack = models.JSONField(default=list)
