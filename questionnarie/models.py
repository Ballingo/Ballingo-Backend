from django.db import models

class Questionnarie(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    sublevel = models.IntegerField()
    questions = models.ManyToManyField('question.Question')

    def __str__(self):
        return self.name




