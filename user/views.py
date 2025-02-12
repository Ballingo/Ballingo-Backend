from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import BallingoUser
from .serializers import BallingoUserSerializer

class SignupView(generics.CreateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.AllowAny]

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            })
        return Response({'error': 'Credenciales inválidas'}, status=400)

class DeleteView(generics.DestroyAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restringe la eliminación para que el usuario solo pueda eliminar su propia cuenta"""
        return BallingoUser.objects.filter(id=self.request.user.id)
    
class UpdateView(generics.UpdateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restringe la actualización para que el usuario solo pueda modificar su propia cuenta"""
        return BallingoUser.objects.filter(id=self.request.user.id)