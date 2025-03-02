from rest_framework import serializers
from .models import GamePack
from shopItem.serializers import ShopItemSerializer

class GamePackSerializer(serializers.ModelSerializer):
    items = ShopItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = GamePack
        fields = '__all__'