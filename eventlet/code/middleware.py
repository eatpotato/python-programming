#!/usr/bin/python
# -*- coding: UTF-8 -*-

from webob import Response
from webob.dec import wsgify
from webob import exc
import webob

class Auth(object):

    def __init__(self, app):
        self.app = app

    #工厂方法
    @classmethod
    def factory(cls, global_config, **local_config):
        def _factory(app):
            return cls(app)
        return _factory

    #__call__方法，实现auth过滤器的功能逻辑
    @wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        resp = self.process_request(req)
        #如果为空，说明认证失败，返回空
        if resp:
            return resp
        return req.get_response(self.app)

    def process_request(self, req):
        if req.headers.get('X-Auth-Token') != 'test':
            return exc.HTTPForbidden()
