from django.conf.urls.defaults import *

urlpatterns = patterns('acm.cabinet.views',
	(r'^$', 'order'),
	(r'^order$', 'order'),
	(r'^add_credit$', 'add_credit'),
	(r'^suggest$', 'suggest'),
	(r'^checkout$', 'checkout'),
)
