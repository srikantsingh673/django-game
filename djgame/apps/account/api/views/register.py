from django.utils.http import url_has_allowed_host_and_scheme
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, resolve_url
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib import messages
from django.conf import settings


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(settings.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        messages.success(self.request, f'Welcome, {user.username}! Your account is ready.')
        return redirect(self.get_success_url())

    def get_success_url(self):
        # Same as login: honour a safe ?next= so sign-up from a protected page returns there
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url and url_has_allowed_host_and_scheme(
            next_url,
            allowed_hosts={self.request.get_host()},
            require_https=self.request.is_secure(),
        ):
            return next_url
        return resolve_url(settings.LOGIN_REDIRECT_URL)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.POST.get('next') or self.request.GET.get('next', '')
        return context
