from rest_framework import viewsets
from .models import Questionnarie
from .serializers import QuestionnarieSerializer

class QuestionnarieViewSet(viewsets.ModelViewSet):
    queryset = Questionnarie.objects.all()
    serializer_class = QuestionnarieSerializer