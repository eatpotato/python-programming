#!/usr/bin/python
# -*- coding: UTF-8 -*-

from webob import Response
from webob import Request
from webob.dec import wsgify
from webob import exc

class Hello(object):

    @wsgify(RequestClass=Request)
    def __call__(self, request):
        return Response('Hello World!\n')

def app_factory(global_config, **local_config):
    return Hello()
