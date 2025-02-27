from django.urls import path, re_path
from .views import SignupView, LoginView, DeleteView, UpdateView, LogoutView, GetView

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('get/<int:pk>', GetView.as_view(), name='get'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('logout', LogoutView.as_view(), name='logout'),
]