from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=200)
    correct_answer = models.IntegerField()
    answers = models.JSONField(default=list)

    def __str__(self):
        return self.title
    