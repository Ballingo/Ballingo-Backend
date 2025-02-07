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
]
