from rest_framework import viewsets
from .models import Food
from .serializer import FoodSerializer

# Create your views here.

# This automatically generates the CRUD operations (GET/POST/PUT/DELETE) 
class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
