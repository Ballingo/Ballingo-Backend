from rest_framework import serializers
from .models import FoodList

class FoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodList
        fields = '__all__'