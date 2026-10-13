from django.shortcuts import get_object_or_404
from djgame.apps.game.models.game import Game
from django.http import HttpResponse
from django.views import View


class GameScriptView(View):
    """
    Serves a game's JavaScript straight from the database.
    """

    def get(self, request, slug):
        game = get_object_or_404(Game.objects.only('code'), slug=slug, is_active=True)
        return HttpResponse(game.code, content_type='text/javascript; charset=utf-8')
