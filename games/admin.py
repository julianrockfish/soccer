from django.contrib import admin
from .models import Game  # Import the Game model

admin.site.register(Game)  # Register it so it appears in the admin panel