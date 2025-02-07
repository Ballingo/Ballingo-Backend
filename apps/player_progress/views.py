from rest_framework import viewsets
from .models import PlayerProgress
from .serializer import PlayerProgressSerializer

# Create your views here.

class PlayerProgressViewSet(viewsets.ModelViewSet):
    serializer_class = PlayerProgressSerializer
    queryset = PlayerProgress.objects.all()
