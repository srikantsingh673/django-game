from djgame.apps.account.api.views.profile import ProfileView
from djgame.apps.account.api.views.logout import LogoutView
from djgame.apps.account.api.views.login import LoginView

from django.urls import path


urlpatterns = [

    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'profile/',
        ProfileView.as_view(),
        name='profile'
    ),
]
