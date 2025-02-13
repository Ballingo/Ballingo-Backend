from rest_framework import viewsets
from .models import ShopItem
from .serializers import ShopItemSerializer

class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer