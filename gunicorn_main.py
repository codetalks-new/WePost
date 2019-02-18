# coding: utf-8
import sys
from gunicorn.app.wsgiapp import WSGIApplication

__author__ = 'banxi'


if __name__ == '__main__':
    app = WSGIApplication("%(prog)s [OPTIONS] [APP_MODULE]")
    sys.exit(app.run())

