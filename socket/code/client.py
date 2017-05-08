#!/usr/bin/python
# -*- coding: UTF-8 -*-
import socket
import time

if __name__ == '__main__':
    #创建socket对象
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #连接本地的8888端口
    sock.connect(('localhost',8888))
    time.sleep(2)
    #向服务器发送字符‘123’
    sock.send(b'123')
    #打印从服务器接受的数据
    print(sock.recv(1024).decode('utf-8'))
    sock.close()

