from django.urls import path, re_path
from .views import SignupView, LoginView, DeleteView, UpdateView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
]