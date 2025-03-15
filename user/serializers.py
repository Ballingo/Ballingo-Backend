from rest_framework import serializers
from .models import BallingoUser
from django.contrib.auth.hashers import make_password
from inventory.models import Inventory
from wardrobe.models import Wardrobe
from foodList.models import FoodList
from player.models import Player

class BallingoUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = BallingoUser 
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = BallingoUser(**validated_data)
        if password:
            if password.startswith('pbkdf2_'):
                user.password = password
            else:
                user.set_password(password)
        user.save()

        wardrobe = Wardrobe.objects.create()
        food_list = FoodList.objects.create()
        inventory = Inventory.objects.create(clothes_inventory=wardrobe, food_inventory=food_list)
        player = Player.objects.create(user=user, inventory=inventory)

        wardrobe.player = player
        wardrobe.save()
        food_list.player = player
        food_list.save()
        
        return user
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.get('password')
            if not password.startswith('pbkdf2_'):
                validated_data['password'] = make_password(password)
        return super().update(instance, validated_data)
    