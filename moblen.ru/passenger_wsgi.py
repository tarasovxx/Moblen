# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2258032/data/www/moblen.ru/Moblen')
sys.path.insert(1, '/var/www/u2258032/data/djangoenv/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'Moblen.conf.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
