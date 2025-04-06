from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from games import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.list_games, name='home'),  # Add a default route
    path('games/', views.list_games, name='list_games'),
    path('games/create/', views.create_game, name='create_game'),
    path('games/update/<int:pk>/', views.update_game, name='update_game'),
    path('games/delete/<int:pk>/', views.delete_game, name='delete_game'),
]

# Add this at the end of the file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)