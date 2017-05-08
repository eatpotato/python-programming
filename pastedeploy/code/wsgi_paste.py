#!/usr/bin/python
# -*- coding: UTF-8 -*-

from webob import Response
from webob.dec import wsgify
from paste import httpserver
from paste.deploy import loadapp
import os
import sys

#这里假设api-paste.ini文件与wsgi_paste.ini在同一目录
ini_path = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, 'api-paste.ini'))

#应用程序
@wsgify
def application(request):
    return Response('Hello World!')

#应用程序工厂方法
def app_factory(global_config, **local_config):
    return application

#判断api-paste.ini是否存在
if not os.path.exists(ini_path):
    print("Cannot find api-paste.ini \n")
    exit(1)

wsgi_app = loadapp('config:' + ini_path)
#启动WSGI服务
httpserver.serve(wsgi_app, host='127.0.0.1', port=8888)

