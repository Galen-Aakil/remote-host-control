#coding:gb2312

import base64
from socket import *

def listen_ip():
    print('���ǽ�ʦ�ˣ�')
    HOST = ''
    PORT = 8881
    BUFSIZ = 1024
    ADDR = (HOST, PORT)  # �����˿ڣ��涨��������С
    s = socket(AF_INET, SOCK_STREAM)  # ����TCP socket����
    s.bind(ADDR)  # �󶨵�ַ
    s.listen(10)  # ����TCP��10��������ϵͳ���Թ���(δ��������ʱ�ȴ�״̬)�����������������ֵ����Ϊ1
    while 1:
        print("�ȴ�����...")
        client, addr = s.accept()  # ��ʼ��������TCP�ͻ��˵����ӡ�
        print('���ӵĵ�ַ', addr)
        while 1:
            data = client.recv(BUFSIZ).decode()  # ����TCP���� decode�����ڴ˴�����bytes������ str����
            print("���յ����ݣ�", data)
            if not data:
                break
            data = input("�����Ҫ�Ͽ���ѧ�������ӣ������롮disconnect��,�������������ѧ������ʾ��Ϣ��")
            client.send(data.encode())  # �Ѵӿͻ��˽����������ݣ��ٷ��͸��ͻ��ˣ������յ�����Ϣ
        client.close()
    s.close()

if __name__=="__main__":
    pass


