from djgame.apps.base.models.base import ModelAbstractBase
from django.conf import settings
from django.db import models


#-------------------------------------------------------------------------------
# GameData
#-------------------------------------------------------------------------------
class GameData(ModelAbstractBase):
    """
    Game state of a user, stored as JSON. One record per user.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='game_data',
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

    def __str__(self):
        return f'Game data for {self.user}'
