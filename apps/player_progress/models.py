from django.db import models
from ..user.models import User
from ..questionarie.models import Questionarie

# Create your models here.

class PlayerProgress(models.Model):
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    date_completed = models.DateTimeField(null=True, blank=True)
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    qustionarie_fk = models.ForeignKey(Questionarie, on_delete=models.CASCADE)
