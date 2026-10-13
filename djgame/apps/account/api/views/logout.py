from django.contrib.auth.views import LogoutView as AuthLogoutView


class LogoutView(AuthLogoutView):
    """
    Logs the user out (POST only) and redirects to LOGOUT_REDIRECT_URL.
    """
