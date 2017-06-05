#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess

if __name__ == '__main__':
    p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate()
    if p.returncode in (0,):
        print 'Success!'
