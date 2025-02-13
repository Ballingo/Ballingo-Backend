from rest_framework import serializers
from .models import GamePack

class GamePackSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePack
        fields = '__all__'