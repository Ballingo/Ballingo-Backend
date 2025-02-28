from rest_framework import serializers
from .models import Wardrobe
from clothes.serializers import ClothesSerializer

class WardrobeSerializer(serializers.ModelSerializer):
    items = ClothesSerializer(many=True, read_only=True)

    class Meta:
        model = Wardrobe
        fields = '__all__'