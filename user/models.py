from django.contrib.auth.models import AbstractUser
from django.db import models

class BallingoUser(AbstractUser):
    email = models.EmailField(unique=True)

    def str(self):
        return self.username
