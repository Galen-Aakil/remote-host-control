# coding:utf-8

import os
def shutdown():
# popen返回文件对象，跟open操作一样
    f = os.popen(r'', "r")

    d = f.read()  # 读文件
    print(d)
    print(type(d))
    f.close()
