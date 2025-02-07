from rest_framework import viewsets
from .models import Shop
from .serializer import ShopSerializer

# Create your views here.

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.all()
