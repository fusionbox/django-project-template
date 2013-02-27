from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy

urlpatterns = patterns('accounts.views',
        url(r'^login/$', 'login', name='login'),
        )

# Login/Logout/Password change and recovery
urlpatterns += patterns('django.contrib.auth.views',
        url(r'^logout/$', 'logout_then_login', name='logout'),
        url(r'^logged-out/$', 'logout'),
        url(r'^password-reset/$', 'password_reset', {
            'post_reset_redirect': reverse_lazy('login_reset_done'),
            'template_name': 'registration/password_reset_form.html',
            'email_template_name': 'registration/password_reset_email.html',
            }, name='login_reset'),
        url(r'^password-reset/done/$', 'password_reset_done', {
            'template_name': 'registration/password_reset_done.html',
            }, name='login_reset_done'),
        url(r'^password-reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
            'password_reset_confirm', {
            'post_reset_redirect': reverse_lazy('login_reset_complete'),
            'template_name': 'registration/password_reset_form.html',
            }, name='login_reset_token'),
        url(r'^passwors-reset/complete/$', 'password_reset_complete', {
            'template_name': 'registration/password_reset_complete.html',
            }, name='login_reset_complete'),
        )
