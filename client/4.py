# -*- coding: utf-8 -*-
import socket

# 创建套接字
s = socket.socket()
# 连接套接字，ip和端口必须是服务器上的
s.connect(('192.168.43.57', 9999))
while True:
    data = input("输入发送消息:")
    if 'q' == data:
        s.close()
        break
    s.send(data.encode())
    # print('接受服务器返回的消息：', s.recv(1024))
# s.close()