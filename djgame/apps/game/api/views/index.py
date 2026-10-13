from djgame.apps.game.models.game import Game
from django.views.generic import ListView


class IndexView(ListView):
    template_name = 'game/index.html'
    context_object_name = 'games'
    queryset = Game.objects.filter(is_active=True).defer('code')
