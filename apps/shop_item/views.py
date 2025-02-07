from rest_framework import viewsets
from .models import ShopItem
from .serializer import ShopItemSerializer

# Create your views here.

class ShopItemViewSet(viewsets.ModelViewSet):
    serializer_class = ShopItemSerializer
    queryset = ShopItem.objects.all()
