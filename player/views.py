from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GetPlayerByUserView(APIView):
    def get(self, request, user_id):
        try:
            player = Player.objects.get(user__id=user_id)  # Obtener el Player con el user_id
            serializer = PlayerSerializer(player)  # Serializar la respuesta
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            return Response({"error": "No se encontró un jugador para este usuario."}, status=status.HTTP_404_NOT_FOUND)
