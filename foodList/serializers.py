from rest_framework import serializers
from .models import FoodList
from foodItem.serializers import FoodItemSerializer

class FoodListSerializer(serializers.ModelSerializer):
    food_items = FoodItemSerializer(many=True, read_only=True)  # Incluir los alimentos dentro de la lista

    class Meta:
        model = FoodList
        fields = ['id', 'player', 'food_items']