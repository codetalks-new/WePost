# coding: utf-8

import multiprocessing
__author__ = 'banxi'


def num_of_workers():
    return  multiprocessing.cpu_count() * 2 + 1


bind = '0.0.0.0:8000'
workers = num_of_workers()
timeout = 60000

errorlog = '/var/log/wepost/error.log'
loglevel = 'info'
accesslog = '/var/log/wepost/access.log'
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'