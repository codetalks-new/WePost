# coding: utf-8

__author__ = 'banxi'

# noinspection PyUnresolvedReferences
from .base import  *

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,"static")
MEDIA_ROOT = os.path.join(BASE_DIR,"medias")
MEDIA_URL = '/media/'
DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
#     'livereload.middleware.LiveReloadScript',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = ['127.0.0.1','localhost']

