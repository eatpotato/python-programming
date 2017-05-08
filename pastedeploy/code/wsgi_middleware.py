#!/usr/bin/python
# -*- coding: UTF-8 -*-

from webob.dec import wsgify
from webob import exc

#过滤器方法
@wsgify.middleware
def auth_filter(request, app):
    if request.headers.get("X-Auth-Token") != 'test':
        return exc.HTTPForbidden()
    return app(request)

#过滤器工厂方法
def filter_factory(global_config, **local_config):
    return auth_filter
