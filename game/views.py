import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import GameData


def index(request):
    return render(request, 'game/index.html')


@login_required
def profile(request):
    game_data = GameData.objects.filter(user=request.user).first()
    return render(request, 'profile/profile.html', {
        'game_data': game_data,
        'game_data_json': json.dumps(game_data.data, indent=2) if game_data else '',
    })
