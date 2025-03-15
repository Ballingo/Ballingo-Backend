from rest_framework import generics, permissions, status
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .models import BallingoUser
from .serializers import BallingoUserSerializer
from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from utils.utils import generate_recovery_code
from django.contrib.auth.hashers import make_password

class SignupView(generics.CreateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = BallingoUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()  # Crea el usuario
            token, created = Token.objects.get_or_create(user=user)  # Genera el token

            return Response({
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class GetView(generics.RetrieveAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restringe la consulta para que el usuario solo pueda ver su propia información"""
        return BallingoUser.objects.filter(id=self.request.user.id)

class UpdateView(generics.UpdateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restringe la actualización para que el usuario solo pueda modificar su propia cuenta"""
        return BallingoUser.objects.filter(id=self.request.user.id)

class DeleteView(generics.DestroyAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Restringe la eliminación para que el usuario solo pueda eliminar su propia cuenta"""
        return BallingoUser.objects.filter(id=self.request.user.id)

class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]  # Solo usuarios autenticados pueden hacer logout

    def post(self, request):
        try:
            # Eliminar el token del usuario
            request.user.auth_token.delete()
            return Response({"message": "Sesión cerrada correctamente"}, status=status.HTTP_200_OK)
        except:
            return Response({"error": "Error al cerrar sesión"}, status=status.HTTP_400_BAD_REQUEST)

class LastLoginView(generics.RetrieveAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BallingoUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return Response({"last_login": user.last_login})

class SetLastLoginView(generics.UpdateAPIView):
    queryset = BallingoUser.objects.all()
    serializer_class = BallingoUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BallingoUser.objects.filter(id=self.request.user.id)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        user.last_login = now()
        user.save(update_fields=['last_login'])
        return Response({"message": "Last login updated correctly"})

class GetRecoveryCode(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(BallingoUser, email=email)

        if not user.recovery_code:
            return Response({'error': 'No recovery code found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'recovery_code': user.recovery_code}, status=status.HTTP_200_OK)

class ResetUserPassword(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(BallingoUser, email=email)
        
        recovery_code = generate_recovery_code()
        user.recovery_code = recovery_code
        user.save(update_fields=['recovery_code'])

        subject = '🔐 Password Reset Request'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]

        text_message = (
            f"Hello {user.username},\n\n"
            "We received a request to reset your password. Use the following code to reset it:\n\n"
            f"🔢 Your recovery code: {recovery_code}\n\n"
            "If you did not request this, please ignore this email.\n\n"
            "Best regards,\nThe Ballingo Team"
        )

        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
                <div style="max-width: 500px; margin: auto; padding: 20px; border-radius: 10px; background: #f9f9f9; text-align: center;">
                    <h2 style="color: #007bff;">🔐 Password Reset Request</h2>
                    <p>Hello <strong>{user.username}</strong>,</p>
                    <p>We received a request to reset your password. Use the following code to reset it:</p>
                    <p style="font-size: 24px; font-weight: bold; background: #007bff; color: white; padding: 10px; border-radius: 5px; display: inline-block;">
                        {recovery_code}
                    </p>
                    <p>If you did not request this, please ignore this email.</p>
                    <br>
                    <p style="color: #777;">Best regards,<br><strong>The Ballingo Team</strong></p>
                </div>
            </body>
        </html>
        """

        email = EmailMultiAlternatives(subject, text_message, from_email, recipient_list)
        email.attach_alternative(html_message, "text/html")
        email.send(fail_silently=False)

        return Response({'message': 'Email sent with instructions to reset your password'}, status=status.HTTP_200_OK)

    def put(self, request):
        email = request.data.get('email')
        new_password = request.data.get('new_password')

        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(BallingoUser, email=email)

        if not new_password:
            return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)

        user.password = make_password(new_password)
        user.save(update_fields=['password'])

        return Response({'message': 'Password updated correctly'}, status=status.HTTP_200_OK)
