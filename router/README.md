这是一个利用Router实现WSGI服务URL映射的例子

本例的RESTFUL API如下:

|类型|URL|方法|描述|
|--|--|--|--|
|集合操作|/instances|GET|列出集合中的所有虚拟机记录|
|集合操作|/instances|POST|添加一条虚拟机记录|
|个体操作|/instances/{instance_id}|GET|获取一条虚拟机的信息|
|个体操作|/instances/{instance_id}|PUT|更新一条虚拟机的信息|
|个体操作|/instances/{instance_id}|DELETE|删除一条虚拟机记录|
