from django.contrib.auth.views import LoginView as AuthLoginView


class LoginView(AuthLoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True
