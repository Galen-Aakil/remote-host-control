# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shut.ui'
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
from PyQt5 import QtCore, QtGui, QtWidgets

class Uii_Dialog(object):
    def __init__(self, student):
        self.student = student

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(387, 247)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 180, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 50, 330, 15))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 100, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        # self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        # self.pushButton_3.setGeometry(QtCore.QRect(350, 7, 101, 61))
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.pushButton_3.setText('断开')
        # self.pushButton_3.clicked.connect(self.shut)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.shut)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def shut(self):
        import socket
        data = self.lineEdit.text().encode()
        # 创建TCP连接的socket对象,SOCK_STREAM表示为tcp协议类型
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接的地址,为元组，第一个值为字符串类型的ip地址，第二个参数为端口号
        address = ("127.0.0.1", 8883)

        # 建立与服务端的连接
        clientSocket.connect(address)

        clientSocket.sendall(data)
        # 当发送信息为空时，断开与服务器的连接
        clientSocket.close()
        print("连接已断开")


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "选择关闭"))
        self.label.setText(_translate("Dialog", "Input tips："))

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = Uii_Dialog(['0','1'])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())