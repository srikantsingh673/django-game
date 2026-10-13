from django.conf import settings
from django.db import models


class GameData(models.Model):
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_data',
    )
    
    data = models.JSONField(
        default=dict, blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = 'game data'
        verbose_name_plural = 'game data'

    def __str__(self):
        return f'Game data for {self.user}'
