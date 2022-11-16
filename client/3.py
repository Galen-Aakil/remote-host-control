#coding:gb2312

import base64
from socket import *

def listen_ip():
    print('我是教师端！')
    HOST = ''
    PORT = 8881
    BUFSIZ = 1024
    ADDR = (HOST, PORT)  # 创建端口，规定缓冲区大小
    s = socket(AF_INET, SOCK_STREAM)  # 创建TCP socket对象
    s.bind(ADDR)  # 绑定地址
    s.listen(10)  # 监听TCP，10代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
    while 1:
        print("等待连接...")
        client, addr = s.accept()  # 开始被动接受TCP客户端的连接。
        print('连接的地址', addr)
        while 1:
            data = client.recv(BUFSIZ).decode()  # 接受TCP数据 decode是由于此处接受bytes而不是 str类型
            print("接收到数据：", data)
            if not data:
                break
            data = input("如果需要断开该学生的连接，请输入‘disconnect’,或者任意输入给学生的提示信息：")
            client.send(data.encode())  # 把从客户端接收来的数据，再发送给客户端，表明收到了信息
        client.close()
    s.close()

if __name__=="__main__":
    pass


