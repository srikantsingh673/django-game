from django.contrib.auth.mixins import LoginRequiredMixin
from djgame.apps.game.models.game_data import GameData
from django.views.generic import TemplateView
import json


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        saves = GameData.objects.filter(user=self.request.user).select_related('game').order_by('-updated')
        for save in saves:
            save.json = json.dumps(save.data, indent=2)
        context['saves'] = saves
        return context
