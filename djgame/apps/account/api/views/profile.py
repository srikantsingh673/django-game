from django.contrib.auth.mixins import LoginRequiredMixin
from djgame.apps.game.models.game_data import GameData
from django.views.generic import TemplateView
import json


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        game_data = GameData.objects.filter(user=self.request.user).first()
        context['game_data'] = game_data
        context['game_data_json'] = json.dumps(game_data.data, indent=2) if game_data else ''
        return context
