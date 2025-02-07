from django.db import models

# Create your models here.

class Language(models.Model):
    questionaries = models.JSONField(default=list)
