#!/usr/bin/python
# -*- coding: UTF-8 -*-

from ftplib import FTP

bufsize = 1024

def HELP():
    print '''
    cd     进入文件夹
    delete 删除文件
    dir    获取当前文件列表
    get    下载文件
    help   帮助
    mkdir  创建文件夹
    put    上传文件
    pwd    获取当前目录
    quit   退出
    rename 重命名文件
    rmdir  删除文件夹
    size   获取文件大小
    '''

def GET(filename):
    command = 'RETR ' + filename
    ftp.retrbinary(command, open(filename, 'wb').write, bufsize)
    print '下载成功'

def PUT(filename):
    command = 'STOR' + filename
    filehandler = open(filename, 'rb')
    ftp.storbinary(command,filehandler,bufsize)
    filehandler.close()
    print '上传成功'

def PWD():
    print ftp.pwd()

if __name__ == '__main__':
    #server = raw_input('输入ftp地址:')
    server = '90.147.160.69'
    ftp = FTP(server)
    actions = {'dir': ftp.dir, 'pwd': PWD, 'cd': ftp.cwd, 'get': GET, 'put': PUT,
               'help': HELP, 'rmdir': ftp.rmd, 'mkdir': ftp.mkd, 'delete': ftp.delete,
               'rename': ftp.rename}
    username = 'anonymous'
    password = ''
    ftp.login(username, password)
    HELP()
    while True:
        print 'pyftp>',
        cmds = raw_input()
        cmd = cmds.split(' ')
        try:
            if len(cmd) == 1:
                if cmd[0] == 'quit':
                    break
                else:
                    actions[cmd[0]]()
            elif len(cmd) == 2:
                actions[cmd[0]](cmd[1])
            elif len(cmd) == 3:
                actions(cmd[0])(cmd[1],cmd[2])
            else:
                print '输入错误'
        except:
            print '命令出错'
    ftp.quit()
