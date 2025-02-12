from rest_framework import serializers
from .models import BallingoUser
from django.contrib.auth.hashers import make_password

class BallingoUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BallingoUser 
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = BallingoUser.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        """Actualizar usuario y encriptar contraseña si se proporciona"""
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)
    