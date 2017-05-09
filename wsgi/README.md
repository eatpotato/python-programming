这是一个使用wsgi部署web服务的小例子

各类含义如下:

|类名|所属文件|描述|
|--|--|--|--|
|Auth|middleware.py|实现Auth过滤器的类|
|Hello|app.py|实现hello应用程序的类|
|WSGIService|service.py|用于WSGI服务的管理，包括服务的启动、停止和监听|
|Loader|wsgi.py|用于加载服务的应用程序|
|SERVER|wsgi.py|实现一个WSGI服务，主要实现对县城的创建、配置和管理|
