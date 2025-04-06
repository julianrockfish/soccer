from django.db import models

class Game(models.Model):
    date = models.DateField()
    opponent = models.CharField(max_length=100)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    final_score = models.CharField(max_length=20)  # Example: "3-1 Win"
    media = models.FileField(upload_to="game_media/", blank=True, null=True)

    class Meta:  # ← Properly indented now
        ordering = ['-date']  # Orders games by date, most recent first

    def __str__(self):
        return f"{self.date} vs {self.opponent}"