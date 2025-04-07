Soccer Tracker
Video Demo: URL will go here
Description:
Soccer Tracker is a Django web application that I will use to record and track my sons game performances. I will use it to log match details, personal statistics, and upload media from his games.

Features

Record game details (date, opponent, score, goals, assists)
Upload photos and videos from games
View performance history in chronological order
Responsive design works on all devices
Admin interface for data management
Secure access controls for data modification

Project Structure
Core Files

manage.py: Django's command-line utility
soccer_tracker/settings.py: Configuration settings
soccer_tracker/urls.py: URL routing definitions

Games App

games/models.py: Defines the Game data model
games/views.py: Contains CRUD operations for game records
games/forms.py: Form for game creation and editing
games/admin.py: Admin interface registration

Templates

games/templates/games/base.html: Base layout and navigation - did not apply bootstrap throughout yet
games/templates/games/list_games.html: Table of all games
games/templates/games/game_detail.html: Single game details
games/templates/games/create_game.html: New game form
games/templates/games/update_game.html: Edit game form
games/templates/games/delete_game.html: Deletion confirmation

Design Decisions
I focused on tracking the most relevant soccer stats (goals and assists) to keep the interface simple yet useful. The media upload feature lets players save memorable moments from my sons games. I started to implemented a Bootstrap-based template for consistent styling and mobile responsiveness but did not finish.
Security was addressed by restricting data modification to authenticated staff members, while allowing anyone to view the statistics.

Future Improvements

User accounts for multiple players
Statistics dashboard with performance visualizations
Team management features
Search and filtering capabilities
Social media sharing

Setup

Clone the repository
Install dependencies: pip install -r requirements.txt
Apply migrations: python manage.py migrate
Create a superuser: python manage.py createsuperuser
Run server: python manage.py runserver
Access at http://localhost:8000

Technologies

Django
SQLite (development) / PostgreSQL (production)
Bootstrap
HTML/CSS
