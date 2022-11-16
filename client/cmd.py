# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cmd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from socket import *
import socket
from PyQt5 import QtCore, QtGui, QtWidgets

class cmd_Dialog(object):
    def __init__(self, addr):
        self.addr = addr

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(60, 340, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(80, 100, 221, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 72, 15))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 140, 321, 200))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setLineWrapMode(1)
        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(self.cmd)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "命令"))
        self.label.setText(_translate("Dialog", "输入命令："))

    def cmd(self):
        import socket
        temp = self.lineEdit.text()
        data = self.lineEdit.text().encode()
        # 创建TCP连接的socket对象,SOCK_STREAM表示为tcp协议类型
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 连接的地址,为元组，第一个值为字符串类型的ip地址，第二个参数为端口号
        address = ("127.0.0.1", 8882)

        # 建立与服务端的连接
        clientSocket.connect(address)

        clientSocket.sendall(data)
        if temp == 'ipconfig/release':
            return
        else:
            re = clientSocket.recv(100000)
        self.textEdit.setText(re.decode())
        # 当发送信息为空时，断开与服务器的连接
        clientSocket.close()
        print("连接已断开")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QDialog()
    ui = cmd_Dialog(['0', '1'])
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())