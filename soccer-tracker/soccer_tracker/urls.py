"""
URL configuration for soccer_tracker project.

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
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from games import views

urlpatterns = [
    # Your existing paths here
    path('games/', views.list_games, name='list_games'),
    path('games/create/', views.create_game, name='create_game'),
    path('games/update/<int:pk>/', views.update_game, name='update_game'),
    path('games/delete/<int:pk>/', views.delete_game, name='delete_game'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path("admin/", admin.site.urls),
]
