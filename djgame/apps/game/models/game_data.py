from djgame.apps.base.models.base import ModelAbstractBase
from djgame.apps.game.models.game import Game
from django.conf import settings
from django.db import models


#-------------------------------------------------------------------------------
# GameData
#-------------------------------------------------------------------------------
class GameData(ModelAbstractBase):
    """
    A user's saved state for one game, stored as JSON. One record per user per game.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_data',
    )

    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='saves',
    )

    data = models.JSONField(
        default=dict, blank=True
    )

    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        verbose_name = 'game data'
        verbose_name_plural = 'game data'
        constraints = [
            models.UniqueConstraint(fields=['user', 'game'], name='one_save_per_user_per_game'),
        ]

    def __str__(self):
        return f'{self.game} save for {self.user}'
