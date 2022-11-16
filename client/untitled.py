# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import *
import os
import threading
import cv2
from shut import *
from luping import *
import socket
import base64
from accepting import *
from cmd import *


class childWindow(QDialog):
    def __init__(self, student):
        QDialog.__init__(self)
        self.child=Uii_Dialog(student)
        self.child.setupUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1000)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap("./ico.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1900, 830))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # self.DispalyLabel = QtWidgets.QLabel(self.tab)
        # self.DispalyLabel.setGeometry(QtCore.QRect(30, 10, 720, 405))
        # self.DispalyLabel.setObjectName("DispalyLabel")
        self.tabWidget.addTab(self.tab, "")
        # self.DispalyLabel.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        self.DispalyLabel2 = QtWidgets.QLabel(self.tab)
        self.DispalyLabel2.setGeometry(QtCore.QRect(20, 20, 1000, 563))
        self.DispalyLabel2.setObjectName("DispalyLabel2")

        self.DispalyLabel2.setStyleSheet("QLabel{border:2px solid rgb(0, 0, 0);}")
        # self.DispalyLabel3 = QtWidgets.QLabel(self.tab)
        # self.DispalyLabel3.setGeometry(QtCore.QRect(30, 425, 720, 405))
        # self.DispalyLabel3.setObjectName("DispalyLabel3")
        #
        # self.DispalyLabel3.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        # self.DispalyLabel4 = QtWidgets.QLabel(self.tab)
        # self.DispalyLabel4.setGeometry(QtCore.QRect(780, 425, 720, 405))
        # self.DispalyLabel4.setObjectName("DispalyLabel4")
        #
        # self.DispalyLabel4.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")

        # self.tab_2 = QtWidgets.QWidget()
        # self.tab_2.setObjectName("tab_2")
        # self.tabWidget.addTab(self.tab_2, "")
        # self.Label = QtWidgets.QLabel(self.tab_2)
        # self.Label.setGeometry(QtCore.QRect(30, 10, 720, 405))
        # self.Label.setObjectName("DispalyLabel")
        # self.Label.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        #
        # self.Label2 = QtWidgets.QLabel(self.tab_2)
        #
        # self.Label2.setGeometry(QtCore.QRect(780, 10, 720, 405))
        # self.Label2.setObjectName("DispalyLabel2")
        #
        # self.Label2.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        # self.Label3 = QtWidgets.QLabel(self.tab_2)
        # self.Label3.setGeometry(QtCore.QRect(30, 425, 720, 405))
        # self.Label3.setObjectName("DispalyLabel3")
        #
        # self.Label3.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        # self.Label4 = QtWidgets.QLabel(self.tab_2)
        # self.Label4.setGeometry(QtCore.QRect(780, 425, 720, 405))
        # self.Label4.setObjectName("DispalyLabel4")
        #
        # self.Label4.setStyleSheet("QLabel{border:2px solid rgb(0, 255, 0);}")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(28, 955, 701, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("QTextBrowser{border-width:0;border-style:outset}")

        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(70, 7, 101, 61))
        # self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.Get_Data)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 850, 101, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 850, 101, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 833, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.connect_client = []
        self.server = []
        # self.listen_thread = threading.Thread(target=self.video)
        # self.listen_thread.start()
        self.listen_thread2 = threading.Thread(target=self.video2)
        self.listen_thread2.start()
        # self.listen_thread3 = threading.Thread(target=self.video3)
        # self.listen_thread3.start()
        # self.listen_thread4 = threading.Thread(target=self.video4)
        # self.listen_thread4.start()

        # self.pack_thread = threading.Thread(target=self.pack)
        # self.pack_thread.start()

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Latrodectus"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "监控"))
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "访问"))
        # self.pushButton.setText(_translate("MainWindow", "监控桌面"))
        self.pushButton_2.setText(_translate("MainWindow", "cmd"))
        self.pushButton_3.setText(_translate("MainWindow", "tips"))

        # self.tabWidget.currentChanged.connect(self.tabWidgetClock)

    def teacher(self, i):
        i=i-i
        self.student = []
        print('我是教师端！')
        HOST = ''
        PORT = 8881
        BUFSIZ = 1024
        tADDR = (HOST, PORT)  # 创建端口，规定缓冲区大小
        monitor = socket.socket(AF_INET, SOCK_STREAM)  # 创建TCP socket对象
        monitor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        monitor.bind(tADDR)  # 绑定地址
        monitor.listen(10)  # 监听TCP，10代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
        while 1:
            print("等待连接...")
            client, addr = monitor.accept()  # 开始被动接受TCP客户端的连接。
            print('连接的地址', addr)
            self.create(client, i)
            self.student.append(client)
            i+=1
        monitor.close()

    def create(self, client, i):
        student_thread = threading.Thread(target=self.recv_student, args=(client, i))
        student_thread.start()

    # def get_student(self):
    #     return self.student

    def recv_student(self, client, i):
        while 1:
            data = client.recv(1024).decode()  # 接受TCP数据 decode是由于此处接受bytes而不是 str类型
            self.show_status(data, i + 1)
            print("接收到数据：", data)
            if not data:
                break
        client.close()

    def pack(self):
        self.teacher(len(self.connect_client))

    def show_status(self, data, i):
        if i==1:
            self.Label.setText(data)
        if i==2:
            self.Label2.setText(data)
        if i==3:
            self.Label3.setText(data)
        if i==4:
            self.Label4.setText(data)

    def tabWidgetClock(self, index):
        if (index == 0):  # 如果点击的是第一个按钮
            pass
        if (index == 1):  # 第二个

            self.cnt()

    # def cnt(self):
    #     while 1:
    #         self.textBrowser.setText('当前连接数：{}'.format(len(self.connect_client)))
    #         import time
    #         time.sleep(0.2)

    def video(self):
        self.isCamera = True
        self.port = 8880
        self.camera = Camera_Connect_Object(("", self.port), 888)
        self.server.append(self.camera)
        self.camera.addr_port = tuple(self.camera.addr_port)

        print('正在等待连接')
        client, D_addr = self.camera.server.accept()
        print(D_addr)
        self.ADDR1 = D_addr
        self.connect_client.append(client)
        self.Get_Data(client, 1, self.camera)
        print('连接成功')
        self.camera.server.close()

    def video2(self):
        self.isCamera = True
        self.port = 8999
        self.camera1 = Camera_Connect_Object(("", self.port), 888)
        self.server.append(self.camera1)
        self.camera1.addr_port = tuple(self.camera1.addr_port)

        print('正在等待连接')
        client1, D_addr = self.camera1.server.accept()
        print(D_addr)
        self.ADDR2 = D_addr
        self.connect_client.append(client1)
        self.Get_Data(client1, 2, self.camera1)
        print('连接成功')
        self.camera1.server.close()

    def video3(self):
        self.isCamera = True
        self.port = 8998
        self.camera2 = Camera_Connect_Object(("", self.port), 888)
        self.server.append(self.camera2)
        self.camera2.addr_port = tuple(self.camera2.addr_port)

        print('正在等待连接')
        client2, D_addr = self.camera2.server.accept()
        print(D_addr)
        self.ADDR3 = D_addr
        self.connect_client.append(client2)
        self.Get_Data(client2, 3, self.camera2)
        print('连接成功')
        self.camera2.server.close()

    def video4(self):
        self.isCamera = True
        self.port = 8997
        self.camera3 = Camera_Connect_Object(("", self.port), 888)
        self.server.append(self.camera3)
        self.camera3.addr_port = tuple(self.camera3.addr_port)

        print('正在等待连接')
        client3, D_addr = self.camera3.server.accept()
        print(D_addr)
        self.ADDR4 = D_addr
        self.connect_client.append(client3)
        self.Get_Data(client3, 4, self.camera3)
        print('连接成功')
        self.camera3.server.close()

    def check_label(self, label):
        if label == 1:
            return self.DispalyLabel
        elif label == 2:
            return self.DispalyLabel2
        elif label == 3:
            return self.DispalyLabel3
        else:
            return self.DispalyLabel4

    def RT_Image(self, client, label, cameraa):
        dislabel = self.check_label(label)
        print('xxxxxxxxx')
        # 按照格式打包发送帧数和分辨率
        name = cameraa.addr_port[0] + " Camera"
        # client.send(str(addr[1]).encode())
        print(cameraa.src, cameraa.resolution[0], cameraa.resolution[1])
        client.send(struct.pack("lhh", cameraa.src, cameraa.resolution[0], cameraa.resolution[1]))
        while (1):
            try:
                info = struct.unpack("lhh", client.recv(8))
                buf_size = info[0]  # 获取读的图片总长度
                if buf_size:
                    try:
                        buf = b""  # 代表bytes类型
                        temp_buf = buf
                        while (buf_size):  # 读取每一张图片的长度
                            temp_buf = client.recv(buf_size)
                            buf_size -= len(temp_buf)
                            buf += temp_buf  # 获取图片
                            # print(type(buf))
                            debs64 = base64.b64decode(buf)
                            data = numpy.fromstring(debs64, dtype='uint8')  # 按uint8转换为图像矩阵
                            image = cv2.imdecode(data, 1)  # 图像解码
                            # cv2.imshow(self.name, self.image)  # 展示图片
                            img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
                            # print('11111111111111')
                            dislabel.setPixmap(QPixmap.fromImage(img))
                    except:
                        pass
                    finally:
                        if (cv2.waitKey(1) == 27):  # 每10ms刷新一次图片，按‘ESC’（27）退出
                            client.close()
                            cv2.destroyAllWindows()
                            break
            except ConnectionResetError as e:
                client.close()
                cv2.destroyAllWindows()
                break
            except TimeoutError as e:
                client.close()
                cv2.destroyAllWindows()
                break

    def Get_Data(self, i, j, k):
        self.threads = []
        showThread = threading.Thread(target=self.RT_Image, args=(i, j, k,))
        self.threads.append(showThread)
        showThread.start()

    def __del__(self):
        return self.server[0]


class parentWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

    # def get(self):
    #     return self.main_ui.get_student()

    def __del__(self):
        return self.main_ui.__del__()

    def getlabel(self, i):
        return self.main_ui.check_label(i)


class acceptWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)


class cmdWindow(QDialog):
    def __init__(self, addr):
        QDialog.__init__(self)
        self.child = cmd_Dialog(addr)
        self.child.setupUi(self)


if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)
    window = parentWindow()
    # display = Display(window)
    # 显示
    student = []
    choose = childWindow(student)
    cmd = cmdWindow(student)
    # accept = acceptWindow()
    # acc = window.main_ui.pushButton
    # acc.clicked.connect(accept.show)
    shutweb = window.main_ui.pushButton_3
    shutweb.clicked.connect(choose.show)
    cmdline = window.main_ui.pushButton_2
    cmdline.clicked.connect(cmd.show)
    window.show()

    sys.exit(app.exec_())
