from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import FormView
from django.views.decorators.debug import sensitive_post_parameters

from fusionbox.views import WithNextUrlMixin


class LoginView(WithNextUrlMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            return redirect(self.get_success_url())
        return super(LoginView, self).get(*args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

login = sensitive_post_parameters('password')(LoginView.as_view())


class LoginRequiredMixin(object):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect(login.with_next(login, self.request.path))
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)
