# coding:utf8
import socket
import threading
import struct
import time
import cv2
import numpy
from PIL import ImageGrab
import numpy as np
import base64

from scapy.sendrecv import sniff
from scapy.utils import wrpcap
import datetime
import dpkt
import os
import subprocess, io


class Carame_Accept_Object:
    def __init__(self, S_addr_port):
        self.resolution = (1920, 1080)  # 分辨率
        self.img_fps = 20  # 每秒传输多少帧数
        self.src = 888 + 30  # 双方确定传输帧数，（888）为校验值
        self.interval = 0  # 图片播放时间间隔
        self.addr_port = S_addr_port
        # self.Set_Socket(S_addr_port)

    # 设置套接字
    def Set_Socket(self, addr_port_t):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口可复用
        self.client.connect(addr_port_t)
        return (self.client, addr_port_t)


def check_option(object, client):
    # 按格式解码，确定帧数和分辨率
    info = struct.unpack('lhh', client.recv(8))
    if info[0] > 888:
        object.img_fps = int(info[0]) - 888  # 获取帧数
        object.resolution = list(object.resolution)
        # 获取分辨率
        object.resolution[0] = info[1]
        object.resolution[1] = info[2]
        object.resolution = tuple(object.resolution)
        return 1
    else:
        return 0


def RT_Image(object, client, D_addr):
    if (check_option(object, client) == 0):
        return
    # camera = cv2.VideoCapture(0)  # 从摄像头中获取视频
    camera = ImageGrab.grab()  # 从摄像头中获取视频
    height, width = camera.size
    # video = cv2.VideoWriter('video02.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))

    img_param = [int(cv2.IMWRITE_JPEG_QUALITY), object.img_fps]  # 设置传送图像格式、帧数

    while (1):
        time.sleep(5)  # 推迟线程运行1s
        captureImage = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)
        # 显示无图像的窗口
        cv2.imshow('capturing', np.zeros((1, 255), np.uint8))

        # 控制窗口显示位置，方便通过按键方式退出
        cv2.moveWindow('capturing', height - 100, width - 100)

        object.img = cv2.resize(frame, object.resolution)  # 按要求调整图像大小(resolution必须为元组)
        _, img_encode = cv2.imencode('.jpg', object.img, img_param)  # 按格式生成图片
        bs64 = base64.b64encode(img_encode)
        img_code = numpy.array(bs64)  # 转换成矩阵
        object.img_data = img_code.tostring()  # 生成相应的字符串
        try:
            # 按照相应的格式进行打包发送图片
            client.send(
                struct.pack("lhh", len(object.img_data), object.resolution[0], object.resolution[1]) + object.img_data)
        except:
            # video.release()
            cv2.destroyAllWindows()
            print("视频连接断开！")
            break
    return


def get_local_ip():
    local_ip = ""
    try:
        socket_objs = [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]
        ip_from_ip_port = [(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in socket_objs][0][1]
        ip_from_host_name = [ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if
                             not ip.startswith("127.")][:1]
        local_ip = [l for l in (ip_from_ip_port, ip_from_host_name) if l][0]
    except (Exception) as e:
        print("get_local_ip found exception : %s" % e)
    return local_ip if ("" != local_ip and None != local_ip) else socket.gethostbyname(socket.gethostname())


def get_ips(ips, pcap):
    for (ts, buf) in pcap:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            # print ('Src:'+src+' -->Dst:'+dst)
            if dst in ips.keys():
                ips[dst] += 1
            else:
                ips[dst] = 1
        except:
            pass
    return ips


def send_to_teacher(ips):
    HOST = '192.168.43.129'  # 服务器的ip
    PORT = 8881  # 需要连接的服务器的端口
    BUFSIZ = 1024  # 缓冲区大小
    ADDR = (HOST, PORT)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义一个TCP连接
    try:
        c.connect(ADDR)
    except:
        print("发送网址警告信息失败！")
    s = "\t访问ip \t\t\t访问次数\n"
    for k in ips.keys():
        s += "\t" + k + " \t\t\t" + str(ips[k]) + "\n"
    data = "学生端" + str(get_local_ip()) + "访问课外页面已超过三次，新增访问情况为：\n" + s
    c.sendall(data.encode())  # 输入文字到‘data’，发送给服务器
    c.close()


def monitor():
    print('这是学生端！')
    HOST = '192.168.43.129'  # 服务器的ip
    PORT = 8881  # 需要连接的服务器的端口
    BUFSIZ = 1024  # 缓冲区大小
    ADDR = (HOST, PORT)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义一个TCP连接
    ips = {}
    LAN_ip = get_local_ip()
    gateway_ip = str(socket.gethostbyname(socket.getfqdn(socket.gethostname())))
    c.connect(ADDR)
    while (1):
        sum = 0
        dpkt1 = sniff(count=10)  # 这里是针对单网卡的机子，多网卡的可以在参数中指定网卡
        wrpcap("demo.pcap", dpkt1)
        f = open('demo.pcap', "rb")
        pcap = dpkt.pcap.Reader(f)
        ips = get_ips(ips, pcap)
        ips[LAN_ip] = 0
        ips[gateway_ip] = 0
        ips.pop(LAN_ip)
        ips.pop(gateway_ip)
        for key in ips.keys():
            sum += ips[key]
        # print(sum,ips)
        if sum >= 3:
            print("访问非教学网站超过三次，已经发送给教师端")
            # 发送给教师端
            s = "\t访问ip \t\t\t访问次数\n"
            for k in ips.keys():
                s += "\t" + k + " \t\t\t" + str(ips[k]) + "\n"
            data = "学生端" + str(get_local_ip()) + "访问课外页面已超过三次，新增访问情况为：\n" + s
            try:
                c.sendall(data.encode())  # 输入文字到‘data’，发送给服务器
            except:
                print("ip监控连接中断！")
                break
            ips = {}
    return


def warning():
    HOST = ''  # 服务器的ip
    PORT = 8883  # 需要连接的服务器的端口
    BUFSIZ = 1024  # 缓冲区大小
    ADDR = (HOST, PORT)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义一个TCP连接
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口可复用
    c.bind(ADDR)
    c.listen(5)
    while (1):
        clientSocket, clientInfo = c.accept()
        data = clientSocket.recv(BUFSIZ).decode()
        os.system('mshta vbscript:msgbox("{}",64,"老师提醒")(window.close)'.format(data))
        # s='msg %username% /time:10 "{}"'.format(data)
        # popen('msg %username% /time:10 "要显示的内容"')
        clientSocket.close()


def popen(cmd):
    try:
        s = ""
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        out, err = p.communicate()
        for line in out.splitlines():
            s += line.decode("gbk", "ignore") + "\n"
        return s
    except BaseException as e:
        return str(e)
    return


def wait_sign():
    HOST = ''  # 服务器的ip
    PORT = 8882  # 需要连接的服务器的端口
    BUFSIZ = 1024  # 缓冲区大小
    ADDR = (HOST, PORT)
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 定义一个TCP连接
    c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口可复用
    c.bind(ADDR)
    c.listen(5)
    while (1):
        clientSocket, clientInfo = c.accept()
        data = clientSocket.recv(BUFSIZ).decode()
        print("接收到的指令为：", data)
        ret = popen(data.strip())
        print(data, "的执行结果为:\n", ret)
        clientSocket.sendall(ret.encode())  # 发送给服务器
        clientSocket.close()


if __name__ == '__main__':
    # 视频传输
    fps = 20
    start = 3  # 延时录制
    end = 15  # 自动结束时间
    camera = Carame_Accept_Object(("192.168.43.129", 8999))
    client, D_addr = camera.Set_Socket(("192.168.43.129", 8999))
    clientThread = threading.Thread(None, target=RT_Image, args=(camera, client, D_addr,))
    clientThread.start()
    print("客户线程已开启！")
    # 监控传输并将异常情况发送给教师端
    # monitor_Thread = threading.Thread(None, target=monitor)
    # monitor_Thread.start()
    # print("监控进程已经开启！")
    ##新建一个进程等待客户端指令
    wait_sign_Thread = threading.Thread(None, target=wait_sign)
    wait_sign_Thread.start()
    print("等待指令进程已经开启！")

    warning_Thread = threading.Thread(None, target=warning)
    warning_Thread.start()
    print("等待提示信息进程已经开启！")


