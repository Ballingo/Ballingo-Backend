from rest_framework import serializers
from .models import ShopItem

class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = "__all__"
