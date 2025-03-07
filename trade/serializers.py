from rest_framework import serializers
from .models import Trade
from food.models import Food
from food.serializers import FoodSerializer
from player.models import Player
from player.serializers import PlayerSerializer

class TradeSerializer(serializers.ModelSerializer):
    # Para lectura (GET), usar el serializador de Food
    in_food = FoodSerializer(read_only=True)
    out_food = FoodSerializer(read_only=True)
    player = PlayerSerializer(read_only=True)

    # Para escritura (POST, PUT), permitir claves foráneas
    in_food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='in_food', write_only=True)
    out_food_id = serializers.PrimaryKeyRelatedField(queryset=Food.objects.all(), source='out_food', write_only=True)
    player_id = serializers.PrimaryKeyRelatedField(queryset=Player.objects.all(), source='player', write_only=True)

    class Meta:
        model = Trade
        fields = ['id', 'player', 'player_id', 'isActive', 'created_at', 'in_food', 'out_food', 'in_food_id', 'out_food_id']
        depth = 1
