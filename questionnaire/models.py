from django.db import models

class Questionnaire(models.Model):
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    unlocked = models.BooleanField(default=False)
    questions = models.ManyToManyField('question.Question')
    language = models.ForeignKey('language.Language', on_delete=models.CASCADE, related_name="questionnaires")

    def __str__(self):
        return self.name




