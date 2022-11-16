# coding:gbk
import socket
import threading
import struct
import time
import cv2
import numpy
from PIL import ImageGrab
import numpy as np


class Carame_Accept_Object:
    def __init__(self, S_addr_port=("", 8880)):
        self.resolution = (1920,1080)  # �ֱ���
        self.img_fps = 20  # ÿ�봫�����֡��
        self.addr_port = S_addr_port
        self.Set_Socket(self.addr_port)

    # �����׽���
    def Set_Socket(self, S_addr_port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # �˿ڿɸ���
        self.server.bind(S_addr_port)
        self.server.listen(5)
        # print("the process work in the port:%d" % S_addr_port[1])


def check_option(object, client):
    # ����ʽ���룬ȷ��֡���ͷֱ���
    info = struct.unpack('lhh', client.recv(8))
    if info[0] > 888:
        object.img_fps = int(info[0]) - 888  # ��ȡ֡��
        object.resolution = list(object.resolution)
        # ��ȡ�ֱ���
        object.resolution[0] = info[1]
        object.resolution[1] = info[2]
        object.resolution = tuple(object.resolution)
        return 1
    else:
        return 0


def RT_Image(object, client, label):
    fps = 20
    if (check_option(object, client) == 0):
        return
    # camera = cv2.VideoCapture(0)  # ������ͷ�л�ȡ��Ƶ
    camera = ImageGrab.grab()  # ������ͷ�л�ȡ��Ƶ
    height, width = camera.size
    video = cv2.VideoWriter('video02.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (height, width))

    img_param = [int(cv2.IMWRITE_JPEG_QUALITY), object.img_fps]  # ���ô���ͼ���ʽ��֡��
    while (1):
        time.sleep(0.1)  # �Ƴ��߳�����0.1s
        captureImage = ImageGrab.grab()
        frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)
        # ��ʾ��ͼ��Ĵ���
        # cv2.imshow('capturing', np.zeros((1, 255), np.uint8))

        # ���ƴ�����ʾλ�ã�����ͨ��������ʽ�˳�
        # cv2.moveWindow('capturing', height-100, width-100)

        object.img = cv2.resize(frame, object.resolution)  # ��Ҫ�����ͼ���С(resolution����ΪԪ��)
        _, img_encode = cv2.imencode('.jpg', object.img, img_param)  # ����ʽ����ͼƬ
        img_code = numpy.array(img_encode)  # ת���ɾ���
        object.img_data = img_code.tostring()  # ������Ӧ���ַ���
        try:
            # ������Ӧ�ĸ�ʽ���д������ͼƬ
            client.send(
                struct.pack("lhh", len(object.img_data), object.resolution[0], object.resolution[1]) + object.img_data)
        except:
            video.release()
            cv2.destroyAllWindows()
            return


if __name__ == '__main__':
    camera = Carame_Accept_Object()
    while (1):
        client, D_addr = camera.server.accept()
        clientThread = threading.Thread(None, target=RT_Image, args=(camera, client, D_addr,))
        clientThread.start()