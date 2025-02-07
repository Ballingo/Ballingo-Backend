from django.db import models

# Create your models here.

class Questionarie(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20)
    questions = models.JSONField(default=list)

    def __str__(self):
        return self.name
