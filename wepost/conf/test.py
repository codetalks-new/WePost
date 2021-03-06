# coding: utf-8

__author__ = 'banxi'

# noinspection PyUnresolvedReferences
from .base import  *

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    'TEST': {
      'NAME': os.path.join(BASE_DIR, 'test_db.sqlite3'),
    }
  }
}
DEBUG = True

PASSWORD_HASHERS = [
  'django.contrib.auth.hashers.MD5PasswordHasher',
]
