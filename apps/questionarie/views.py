from rest_framework import viewsets
from .models import Questionarie
from .serializer import QuestionarieSerializer

# Create your views here.

class QuestionarieViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionarieSerializer
    queryset = Questionarie.objects.all()
