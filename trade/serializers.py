from rest_framework import serializers
from .models import Trade
from food.models import Food  # Importar modelo Food
from food.serializers import FoodSerializer  # Importar FoodSerializer para anidar en GET

class TradeSerializer(serializers.ModelSerializer):
    # Para lectura (GET), usar el serializador de Food
    in_food = FoodSerializer(read_only=True)
    out_food = FoodSerializer(read_only=True)

    # Para escritura (POST, PUT), permitir claves foráneas
    in_food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='in_food', write_only=True)
    out_food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='out_food', write_only=True)

    class Meta:
        model = Trade
        fields = ['id', 'player', 'isActive', 'created_at', 'in_food', 'out_food', 'in_food_id', 'out_food_id']
