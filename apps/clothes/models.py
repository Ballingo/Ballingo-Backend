from django.db import models

# Create your models here.

class Clothes(models.Model):
    type = models.CharField(choices=[('hat', 'Hat'), ('tshirt', 'T-Shirt'), ('shoes', 'Shoes'), ('accessories', 'Accessories')], max_length=50, default='tshirt')
    style = models.ImageField()

    def __str__(self):
        return self.type
