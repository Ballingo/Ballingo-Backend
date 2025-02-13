from rest_framework import viewsets
from .models import PlayerProgress
from .serializers import PlayerProgressSerializer

class PlayerProgressViewSet(viewsets.ModelViewSet):
    queryset = PlayerProgress.objects.all()
    serializer_class = PlayerProgressSerializer
