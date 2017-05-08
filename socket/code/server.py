#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket

if __name__ == '__main__':
    #创建socket对象
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定到本地的8888端口
    sock.bind(('localhost',8888))
    #再本地的8888端口上监听,等待连接队列的最大长度为5
    sock.listen(5)
    while True:
        connection,address = sock.accept()
        try:
            connection.settimeout(5)
            #接受客户端的数据
            buf = connection.recv(1024).decode('utf-8')
            if buf == '123':
                connection.send(b'welcome to server!')
            else:
                connection.send(b'bye bye')
        except socket.timeout:
            print 'time out'
        connection.close()
