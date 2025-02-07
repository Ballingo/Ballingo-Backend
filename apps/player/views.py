from rest_framework import viewsets
from .models import Player
from .serializer import PlayerSerializer

# Create your views here.

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
