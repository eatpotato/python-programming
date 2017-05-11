这是一个使用oslo_config从命令行或者配置文件读取配置并解析的小例子

运行结果:

```
[root@openstack]# python test_oslo_config.py --help
usage: test_oslo_config [-h] [--bind_host BIND_HOST] [--bind_port BIND_PORT]
                        [--config-dir DIR] [--config-file PATH]

optional arguments:
  -h, --help            show this help message and exit
  --bind_host BIND_HOST
                        IP address to listen on.
  --bind_port BIND_PORT
                        Port number to listen on.
  --config-dir DIR      Path to a config directory to pull `*.conf` files
                        from. This file set is sorted, so as to provide a
                        predictable parse order if individual options are
                        over-ridden. The set is parsed after the file(s)
                        specified via previous --config-file, arguments hence
                        over-ridden options in the directory take precedence.
  --config-file PATH    Path to a config file to use. Multiple config files
                        can be specified, with values in later files taking
                        precedence. Defaults to None.

[root@openstack]# python test_oslo_config.py --config-file nova.conf
bind_host: 0.0.0.0, bind_port: 8774
rabbit_host: 127.0.0.1
```

## Option Groups


```
rabbit_group = cfg.OptGroup(name='rabbit',
                            title='RabbitMQ options')
rabbit_host_opt = cfg.StrOpt('host',
                             default='localhost',
rabbit_port_opt = cfg.PortOpt('port',
                              default=5672,
                              help='Port number to listen on.')

def register_rabbit_opts(conf):
    conf.register_group(rabbit_group)
    # options can be registered under a group in either of these ways:
    conf.register_opt(rabbit_host_opt, group=rabbit_group)
    conf.register_opt(rabbit_port_opt, group='rabbit')
```
如果不需要组名称以外的组属性，则该组不需要显式注册

```
def register_rabbit_opts(conf):
    # The group will automatically be created, equivalent calling::
    #   conf.register_group(OptGroup(name='rabbit'))
    conf.register_opt(rabbit_port_opt, group='rabbit')
```

如果不指定组，那么所有的option都属于config 文件的‘DEFAULT’部分

## 参考

[oslo.config](https://docs.openstack.org/developer/oslo.config/cfg.html)

