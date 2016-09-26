import django.views.static
import django.views.generic
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


class SettingsTemplateView(django.views.generic.TemplateView):
    def get_context_data(self, **kwargs):
        context = super(SettingsTemplateView, self).get_context_data(**kwargs)
        context['settings'] = settings
        return context


urlpatterns = [
    url('^robots.txt$', SettingsTemplateView.as_view(
        template_name='robots.txt', content_type='text/plain'
    )),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', django.views.static.serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
