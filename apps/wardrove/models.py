from django.db import models
from ..user.models import User

# Create your models here.

class Wardrove(models.Model):
    items = models.JSONField(default=list)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
