from rest_framework import viewsets
from .models import GamePack
from .serializers import GamePackSerializer

class GamePackViewSet(viewsets.ModelViewSet):
    queryset = GamePack.objects.all()
    serializer_class = GamePackSerializer