from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=True, methods=['put'])
    def update_language(self, request, pk=None):
        """
        Actualiza el campo actualLanguage del jugador.
        """
        player = self.get_object()
        new_language = request.data.get('actualLanguage')

        if new_language not in ['en', 'es', 'de', 'ar', 'ja']:
            return Response({'error': 'Idioma no válido'}, status=status.HTTP_400_BAD_REQUEST)

        player.actualLanguage = new_language
        player.save()

        return Response({'message': 'Idioma actualizado correctamente', 'actualLanguage': player.actualLanguage}, status=status.HTTP_200_OK)


class GetPlayerByUserView(APIView):
    def get(self, request, user_id):
        try:
            player = Player.objects.get(user__id=user_id)  # Obtener el Player con el user_id
            serializer = PlayerSerializer(player)  # Serializar la respuesta
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Player.DoesNotExist:
            return Response({"error": "No se encontró un jugador para este usuario."}, status=status.HTTP_404_NOT_FOUND)
