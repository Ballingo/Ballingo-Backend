from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('api/user/', include('user.urls'))
]
