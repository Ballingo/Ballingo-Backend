from django.db import models

class Clothes(models.Model): # type tiene que ser un ENUM { hat, tshirt, shoes, accesories} y imagen puediendo estar a null
    type = models.CharField(
        choices=[
            ('hat', 'Hat'), 
            ('tshirt', 'T-Shirt'), 
            ('shoes', 'Shoes'), 
            ('accesories', 'Accessories')
        ], 
        max_length=20
    )
    style = models.ImageField(upload_to='clothes/', null=True, blank=True)