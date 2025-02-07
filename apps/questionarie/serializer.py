from rest_framework import serializers
from .models import Questionarie

class QuestionarieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionarie
        fields = '__all__'
