#!/usr/bin/python
# -*- coding: UTF-8 -*-

from paste import httpserver

#定义应用程序
def application(environ, start_response):
    #设置HTTP的应答状态
    start_response('200 OK', [('Content-type', 'text/htmp')])
    #向客户端返回一个字符串
    return ['Hello World\n']
#启动WSGI服务
httpserver.serve(application, host='127.0.0.1',port=8888)
