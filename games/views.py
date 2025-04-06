from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Game
from .forms import GameForm  # You'll create this form in the next step
from django.contrib.admin.views.decorators import staff_member_required  # Import this


# Create Game
@staff_member_required
def create_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Include FILES for media
        if form.is_valid():
            form.save()
            return redirect('list_games')  # Redirect to list view after saving
    else:
        form = GameForm()
    return render(request, 'games/create_game.html', {'form': form})

# Update Game
@staff_member_required
def update_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES, instance=game)
        if form.is_valid():
            form.save()
            return redirect('list_games')
    else:
        form = GameForm(instance=game)
    return render(request, 'games/update_game.html', {'form': form})

# Delete Game
@staff_member_required
def delete_game(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        game.delete()
        return redirect('list_games')
    return render(request, 'games/delete_game.html', {'game': game})

# List Games
def list_games(request):
    games = Game.objects.all()  # Get all games
    return render(request, 'games/list_games.html', {'games': games})


# Detail Game
def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    return render(request, 'games/game_detail.html', {'game': game})

