from django.conf.urls.static import static
from django.urls.conf import include
from django.contrib import admin
from django.conf import settings
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

# Serve uploaded files in development (static() does nothing when DEBUG is False)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
