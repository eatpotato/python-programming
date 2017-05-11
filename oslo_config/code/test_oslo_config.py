#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

from oslo_config import cfg
from oslo_config import types

PortType = types.Integer(1, 65535)

opts = [
    cfg.StrOpt('bind_host',
               default='0.0.0.0',
               help='IP address to listen on.'),
    cfg.Opt('bind_port',
            type=PortType,
            default=8774,
            help='Port number to listen on.')
]
rabbit_host = cfg.StrOpt('rabbit_host',
                         default='localhost',
                         help='IP/hostname to listen on.'),
CONF = cfg.CONF
CONF.register_opts(opts)
CONF.register_opts(rabbit_host, group='oslo_messaging_rabbit')
CONF.register_cli_opts(opts)

if __name__ == '__main__':
    CONF(sys.argv[1:])
    print("bind_host: %s, bind_port: %s" %
          (CONF.bind_host, CONF.bind_port))
    print 'rabbit_host: {}'.format(CONF.oslo_messaging_rabbit.rabbit_host)
