from django.conf.urls.defaults import *

urlpatterns = patterns('acm.membership.views',
	(r'^$', 'register'),
	(r'^register$', 'register'),
	(r'^payment$', 'payment'),
	(r'^account$', 'account'),
	(r'^login$', 'login'),
	(r'^logout$', 'logout'),
)
