from django.db import models

class PlayerProgress(models.Model):
    player = models.ForeignKey('player.Player', on_delete=models.CASCADE, related_name='player_progress')
    questionnaire = models.ForeignKey('questionnaire.Questionnaire', on_delete=models.CASCADE, related_name='player_progress')
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)