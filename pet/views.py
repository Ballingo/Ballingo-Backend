from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from .models import Pet
from .serializers import PetSerializer

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

    # 🔹 Getter para `language`
    @action(detail=True, methods=['get'])
    def get_language(self, request, pk=None):
        pet = self.get_object()
        return Response({"language": pet.language})

    # 🔹 Getter para `hunger`
    @action(detail=True, methods=['get'])
    def get_hunger(self, request, pk=None):
        pet = self.get_object()
        return Response({"hunger": pet.hunger})

    # 🔹 Getter para `is_dead`
    @action(detail=True, methods=['get'])
    def get_is_dead(self, request, pk=None):
        pet = self.get_object()
        return Response({"isDead": pet.isDead})

    # 🔹 Setter para `hunger`
    @action(detail=True, methods=['post'])  # Usa 'post' o 'patch' para modificar valores
    def set_hunger(self, request, pk=None):
        pet = self.get_object()
        hunger_value = request.data.get("hunger")

        if hunger_value is not None:
            try:
                pet.hunger = int(hunger_value)
                pet.save()
                return Response({"message": "Hunger updated successfully", "hunger": pet.hunger}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({"error": "Invalid hunger value"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Missing hunger value"}, status=status.HTTP_400_BAD_REQUEST)

    # 🔹 Setter para `is_dead`
    @action(detail=True, methods=['post'])
    def set_is_dead(self, request, pk=None):
        pet = self.get_object()
        is_dead_value = request.data.get("isDead")

        if is_dead_value is not None:
            pet.isDead = bool(is_dead_value)
            pet.save()
            return Response({"message": "isDead updated successfully", "isDead": pet.isDead}, status=status.HTTP_200_OK)

        return Response({"error": "Missing isDead value"}, status=status.HTTP_400_BAD_REQUEST)