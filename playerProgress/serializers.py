from rest_framework import serializers
from .models import PlayerProgress
from questionnaire.models import Questionnaire

class PlayerProgressSerializer(serializers.ModelSerializer):

    questionnaire = Questionnaire()

    class Meta:
        model = PlayerProgress
        fields = '__all__'
        depth = 1

    