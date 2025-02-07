from django.db import models

# Create your models here.

class Questions(models.Model):
    tittle = models.CharField(max_length=100)
    answers = models.JSONField(default=list)
    correct_answer = models.CharField(max_length=100, null=False, blank=False)
