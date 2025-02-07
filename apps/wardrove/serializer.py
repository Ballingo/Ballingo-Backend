from rest_framework import serializers
from .models import Wardrove

class WardroveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wardrove
        fields = '__all__'
