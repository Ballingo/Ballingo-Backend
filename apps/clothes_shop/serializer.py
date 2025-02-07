from rest_framework import serializers
from .models import ClothesShop

class ClothesShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesShop
        fields = '__all__'
