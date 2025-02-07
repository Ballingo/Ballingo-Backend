from rest_framework import viewsets
from .models import Pet
from .serializer import PetSerializer

# Create your views here.

class PetViewSet(viewsets.ModelViewSet):
    serializer_class = PetSerializer
    queryset = Pet.objects.all()
