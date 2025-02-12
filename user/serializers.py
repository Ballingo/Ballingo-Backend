from rest_framework import serializers
from .models import BallingoUser

class BallingoUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BallingoUser 
        fields = ['id', 'username', 'email', 'telefono', 'direccion', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = BallingoUser.objects.create_user(**validated_data)
        return user