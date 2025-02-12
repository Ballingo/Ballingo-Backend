from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=2)
    hunger_points = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
