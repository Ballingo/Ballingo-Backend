from rest_framework import serializers
from .models import CoinsShop

class CoinsShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoinsShop
        fields = '__all__'
