"""
URL configuration for django_ballingo_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="API DOCUMENTATION",
      default_version='v1',
      description="API Documentation for Ballingo Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="team@ballingo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("food/", include("apps.food.urls")),
    path("clothes/", include("apps.clothes.urls")),
    path("questions/", include("apps.questions.urls")),
    path("coins_shop/", include("apps.coins_shop.urls")),
    path("clothes_shop/", include("apps.clothes_shop.urls")),
    path("shop_item/", include("apps.shop_item.urls")),
    path("shop/", include("apps.shop.urls")),
    path("questionarie/", include("apps.questionarie.urls")),
    path("language/", include("apps.language.urls")),
    path("player/", include("apps.player.urls")),
    path("user/", include("apps.user.urls")),
    path("food_list/", include("apps.food_list.urls")),
    path("food_item/", include("apps.food_item.urls")),
    path("pet/", include("apps.pet.urls")),
    path("wardrove/", include("apps.wardrove.urls")),
    path("player_progress/", include("apps.player_progress.urls")),
    path("trade/", include("apps.trade.urls")),

   path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
   path('redocs/', schema_view.with_ui('redoc', cache_timeout=0)),
]
