from djgame.apps.base.models.base import ModelAbstractBase
from django.core.validators import FileExtensionValidator
from django.db import models


#-------------------------------------------------------------------------------
# Game
#-------------------------------------------------------------------------------
class Game(ModelAbstractBase):
    """
    A playable game. The JavaScript itself is stored in `code`.
    """

    slug = models.SlugField(
        unique=True,
        help_text="Used in the URL: /games/<slug>/"
    )

    title = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    # Images only: SVG / HTML can carry scripts that would run on this site
    thumbnail = models.FileField(
        upload_to='game/thumbnails/',
        blank=True,
        validators=[FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif', 'webp'])],
        help_text="Thumbnail image (PNG, JPG, GIF or WebP)"
    )

    code = models.TextField(
        help_text=(
            'JavaScript for the game. Draw on DjGame.canvas; '
            'use await DjGame.load() and DjGame.save(state) for progress.'
        )
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active games are listed and playable"
    )

    #---------------------------------------------------------------------------
    # Meta
    #---------------------------------------------------------------------------
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
