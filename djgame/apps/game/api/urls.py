from djgame.apps.game.api.views.index import IndexView
from django.urls import path


urlpatterns = [

    path(
        '',
        IndexView.as_view(),
        name='index'
    ),
]
