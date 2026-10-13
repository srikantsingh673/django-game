from django.urls.conf import include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',
         include(
            ('djgame.apps.account.api.urls', 'account'),
            namespace='account'
         )
    ),
    path('',
         include(
            ('djgame.apps.game.api.urls', 'game'),
            namespace='game'
         )
    ),
]
