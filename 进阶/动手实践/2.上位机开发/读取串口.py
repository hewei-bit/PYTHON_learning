# coding=gb18030

import serial  # ����serial��
import time  # ����time��

s = serial.Serial('com4', 115200, timeout=2)  # �򿪴��ڣ������Ǵ�������

while True:  # ����ѭ����ȡ����

    localtime = time.asctime(time.localtime(time.time()))  # time��������ñ���ʱ����÷�
    n = s.readline()  # serial�����÷� ��ȡ���ڵ�һ������
    data_pre = str(n)  # �Ѷ�ȡ������ת�����ַ���
    data = data_pre[2:-3]  # ȡ���ݵ�һ���ַŽ�data����
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), data)  # ��ӡ���ݺ�ʱ��
