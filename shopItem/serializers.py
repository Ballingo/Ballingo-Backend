from rest_framework import serializers
from .models import ShopItem
from clothes.serializers import ClothesSerializer

class ShopItemSerializer(serializers.ModelSerializer):
    clothes = ClothesSerializer(read_only=True)

    class Meta:
        model = ShopItem
        fields = '__all__'