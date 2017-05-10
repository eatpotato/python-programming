#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import pexpect

def ssh_connect():
    if len(sys.argv) != 3:
        print 'USAGE: python {} [username@]HOSTIP PASSWORD'.format(sys.argv[0])
        sys.exit(1)
    else:
        host = sys.argv[1]
        password = sys.argv[2]
        SSH = 'ssh -o StrictHostKeyChecking=no {}'.format(host)
        child = pexpect.spawn(SSH)
        child.expect(['password:'])
        child.sendline(password)
        child.interact()

if __name__ == '__main__':
    ssh_connect()
