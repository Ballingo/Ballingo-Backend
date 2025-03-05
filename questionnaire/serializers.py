from rest_framework import serializers
from .models import Questionnaire
from question.models import Question

class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = Question()

    class Meta:
        model = Questionnaire
        fields = '__all__'
        depth = 1