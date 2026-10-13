from djgame.apps.game.models.game import Game
from django.views.generic import DetailView


class PlayView(DetailView):
    template_name = 'game/play.html'
    context_object_name = 'game'
    queryset = Game.objects.filter(is_active=True).defer('code')
