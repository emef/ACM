import os
import sys

sys.path.append('/home/matt/ACM/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'acm.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
