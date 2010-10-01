from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^cabinet/', include('acm.cabinet.urls')),
    (r'^membership/', include('acm.membership.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 
			'django.views.static.serve', 
			{'document_root': settings.STATIC_MEDIA_ROOT}),
    )

