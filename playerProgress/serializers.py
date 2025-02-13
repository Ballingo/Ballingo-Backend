from rest_framework import serializers
from .models import PlayerProgress

class PlayerProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProgress
        fields = '__all__'