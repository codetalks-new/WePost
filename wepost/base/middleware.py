# coding: utf-8
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.handlers.wsgi import WSGIRequest

__author__ = '代码会说话'

class AuthTokenAwareSessionMiddleware(SessionMiddleware):

    def process_request(self, request:WSGIRequest):
        auth_token = request.META.get("HTTP_X_AUTH_TOKEN")
        if auth_token:
            session_key = auth_token
            request.session = self.SessionStore(session_key)
        else:
            super(AuthTokenAwareSessionMiddleware, self).process_request(request)