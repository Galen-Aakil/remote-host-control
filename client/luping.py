# coding:gbk
# 客户端

from PyQt5.QtGui import QIcon, QImage, QPixmap
import socket
import cv2
import threading
import struct
import numpy


class Camera_Connect_Object:
    def __init__(self, D_addr_port, jiao):
        self.resolution = (1000, 563)
        self.addr_port = D_addr_port
        self.src = jiao + 60  # 双方确定传输帧数，（888）为校验值
        self.interval = 0  # 图片播放时间间隔
        self.img_fps = 60  # 每秒传输多少帧数

        self.Set_Socket(self.addr_port)

    # 设置套接字
    def Set_Socket(self, S_addr_port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 端口可复用
        self.server.bind(S_addr_port)
        self.server.listen(5)

    def __del__(self):
        self.server.close()


if __name__ == '__main__':
    camera = Camera_Connect_Object()
    # camera.addr_port[0]="服务端的ip"
    camera.addr_port = tuple(camera.addr_port)
    camera.Socket_Connect()
    camera.Get_Data(camera.interval)