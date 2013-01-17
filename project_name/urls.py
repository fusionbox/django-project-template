from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.views.generic import TemplateView

from fusionbox.views import StaticServe


urlpatterns = patterns('',
    url('^robots.txt$', StaticServe.as_view(template_name='robots.txt', mimetype='text/plain')),
    #url('^sitemap.xml$', StaticServe.as_view(template_name='sitemap.xml', mimetype='application/xml')),

    # Home
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    # Examples:
    # url(r'^$', '{{ project_name }}.views.home', name='home'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),

    # Accounts URLS
    url(r'^account/', include('accounts.urls')),

    # Admin URLS
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
