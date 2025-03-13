from django.urls import path, re_path
from .views import SignupView, LoginView, DeleteView, UpdateView, LogoutView, GetView, LastLoginView, SetLastLoginView, ResetUserPassword, GetRecoveryCode

urlpatterns = [
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('get/<int:pk>', GetView.as_view(), name='get'),
    path('get/last-login/<int:pk>', LastLoginView.as_view(), name='get_last_login'),
    path('set/last-login/<int:pk>', SetLastLoginView.as_view(), name='set_last_login'),
    path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
    path('update/<int:pk>', UpdateView.as_view(), name='update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('reset-password/request', ResetUserPassword.as_view(), name='reset_password'),
    path('get-recovery-code', GetRecoveryCode.as_view(), name='get_recovery_code'),
    path('confirm-new-password', ResetUserPassword.as_view(), name='reset_password'),
]