from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

handler404 = '{{ project_name }}.views.error404'
handler500 = '{{ project_name }}.views.error500'

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^admin/', include(admin.site.urls)),
) 

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True})
    )

