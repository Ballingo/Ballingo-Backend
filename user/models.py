from django.contrib.auth.models import AbstractUser
from django.db import models

class BallingoUser(AbstractUser):
    email = models.EmailField(unique=True)
    recovery_code = models.CharField(null=True, blank=True)

    def str(self):
        return self.username
