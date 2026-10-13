from djgame.apps.game.api.views.script import GameScriptView
from djgame.apps.game.api.views.index import IndexView
from djgame.apps.game.api.views.save import SaveView
from djgame.apps.game.api.views.play import PlayView
from django.urls import path


urlpatterns = [

    path(
        '',
        IndexView.as_view(),
        name='index'
    ),

    path(
        'games/<slug:slug>/',
        PlayView.as_view(),
        name='play'
    ),

    path(
        'games/<slug:slug>/game.js',
        GameScriptView.as_view(),
        name='script'
    ),

    path(
        'games/<slug:slug>/save/',
        SaveView.as_view(),
        name='save'
    ),
]
