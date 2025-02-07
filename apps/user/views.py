from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
