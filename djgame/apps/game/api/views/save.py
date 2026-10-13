from djgame.apps.game.models.game_data import GameData
from djgame.apps.game.models.game import Game
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
import json


class SaveView(View):
    """
    GET returns the user's saved state for a game; PUT replaces it with the JSON body.
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Log in to save your progress.'}, status=401)
        self.game = get_object_or_404(Game.objects.defer('code'), slug=kwargs['slug'], is_active=True)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, slug):
        save = GameData.objects.filter(user=request.user, game=self.game).first()
        return JsonResponse({'data': save.data if save else None})

    def put(self, request, slug):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Body must be valid JSON.'}, status=400)
        save, _ = GameData.objects.update_or_create(
            user=request.user, game=self.game, defaults={'data': data}
        )
        return JsonResponse({'saved': save.updated.isoformat()})
