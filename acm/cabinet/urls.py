from django.conf.urls.defaults import *

urlpatterns = patterns('acm.cabinet.views',
	(r'^$', 'index'),
)
