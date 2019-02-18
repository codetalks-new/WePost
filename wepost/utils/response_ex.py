# coding: utf-8
from django.http import HttpResponseBadRequest

__author__ = 'banxi'

def http400():
    return HttpResponseBadRequest()

