#!/usr/bin/python
# -*- coding: UTF-8 -*-
import pymysql

if __name__ == '__main__':
    db = pymysql.connect("localhost","root","123","test",charset="utf8")
    cx = db.cursor()
    sql1 = "insert into test (name) values ('test')".encode("utf8")
    sql2 = "select * from test".encode("utf8")
    cx.execute(sql1)
    cx.execute(sql2)
    print(cx.fetchall())
    db.commit()
    db.close()

