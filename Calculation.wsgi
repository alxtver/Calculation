import os
import sys	
sys.path.append('~/projects/Calculation/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Calculation.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
