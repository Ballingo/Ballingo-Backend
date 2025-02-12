from rest_framework import serializers
from .models import Questionnarie

class QuestionnarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnarie
        fields = '__all__'