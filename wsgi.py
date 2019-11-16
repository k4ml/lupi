#!/usr/bin/python
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'lupi.settings'

from lupi.wsgi import application
