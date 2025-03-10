from django.db import models

class Clothes(models.Model): # type tiene que ser un ENUM { hat, tshirt, shoes, accesories} y imagen puediendo estar a null
    type = models.CharField(
        choices=[
            ('hat', 'Hat'),
            ('eyes', 'Eyes'),
            ('shoes', 'Shoes'),
            ('accesories', 'Accessories')
        ], 
        max_length=20
    )
    image_path = models.CharField(max_length=255, blank=True, null=True)