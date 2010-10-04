from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.simple.redirect_to', {'url': '/cabinet/'}),
    (r'^admin/', include(admin.site.urls)),
    (r'^cabinet/', include('acm.cabinet.urls')),
    (r'^membership/', include('acm.membership.urls')),
)


