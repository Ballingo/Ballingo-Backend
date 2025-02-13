from rest_framework import serializers
from .models import RealPack

class RealPackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealPack
        fields = '__all__'