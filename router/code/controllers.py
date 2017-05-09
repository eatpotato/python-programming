#!/usr/bin/python
# -*- coding: UTF-8 -*-

import uuid
import webob
import simplejson
from webob.dec import wsgify

class Controller(object):
    def __init__(self):
        self.instances = {}
        #初始化的时候会创建三条虚拟机的记录
        for i in xrange(3):
            inst_id = str(uuid.uuid4())
            self.instances[inst_id] = {'id': inst_id,
                                       'name': 'inst-' + str(i)}

    def create(self, req):
        print(req.params)
        name = req.params['name']
        if name:
            inst_id = str(uuid.uuid4())
            inst = {'id': inst_id,
                    'name': name}

            self.instances[inst_id] = inst
            return {'instance': inst}

    def show(self, req, instance_id):
        inst = self.instances.get(instance_id)
        return {'instance': inst}

    def index(self, req):
        return {'instances': self.instances.values()}

    def delete(self, req, instance_id):
        if self.instances.get(instance_id):
            self.instances.pop(instance_id)

    def update(self, req, instance_id):
        inst = self.instances.get(instance_id)
        name = req.params['name']
        if inst and name:
            inst['name'] = name
            return {'instance': inst}

    @wsgify(RequestClass=webob.Request)
    def __call__(self, req):
        #获取URL解析结果
        arg_dict = req.environ['wsgiorg.routing_args'][1]
        #或许处理方法
        action = arg_dict.pop('action')
        #删除controller项，剩下的都是参数列表
        del arg_dict['controller']
        #搜索controller类中定义的方法
        method = getattr(self, action)
        #调用方法，处理http请求
        result = method(req, **arg_dict)
        #无返回值
        if result is None:
            return webob.Response(body='',
                                  status='204 Not Found',
                                  headerlist=[('Content-Type',
                                               'application/json')])
        else:
            if not isinstance(result, basestring):
                #将返回值转化成字符串
                result = simplejson.dumps(result)
            return result
