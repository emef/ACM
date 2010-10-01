from django.conf.urls.defaults import *

urlpatterns = patterns('acm.membership.views',
	(r'^$', 'register'),
	(r'^register$', 'register'),
	(r'^account$', 'account'),
)
