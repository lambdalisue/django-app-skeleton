# vim: set fileencoding=utf-8 :
version = (0, 1, 0)
__version__ = '.'.join(map(str, version))

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def checkconf(name, msg):
    """check django.conf.settings is proprely configured"""
    if not hasattr(settings, name):
        raise ImproperlyConfigured(msg)

def setconf(name, default_value):
    """set default value to django.conf.settings"""
    value = getattr(settings, name, default_value)
    setattr(settings, name, value)


