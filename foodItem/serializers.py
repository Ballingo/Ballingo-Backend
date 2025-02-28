from rest_framework import serializers
from .models import FoodItem
from food.serializers import FoodSerializer

class FoodItemSerializer(serializers.ModelSerializer):
    food = FoodSerializer(read_only=True)  # Incluye la información completa del alimento

    class Meta:
        model = FoodItem
        fields = ['id', 'food', 'quantity']  # Devuelve el alimento y la cantidad