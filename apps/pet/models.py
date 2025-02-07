from django.db import models
from ..user.models import User

# Create your models here.

class Pet(models.Model):
    language = models.CharField(max_length=100)
    hunger = models.IntegerField(default=100)
    is_dead = models.BooleanField(default=False)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
