# -*- coding: cp949 -*-
'''
BOB������ C ���� ¥ �������� �̹����� python���� ������ ���ҽ��ϴ�.
pydivert�� windivert�� ���� ����� �� �ְ� ����� python package�̰�
https://github.com/ffalcinelli/pydivert�� �޴����� �ֱ� ������ ������ package ��ġ��
pip install pydivert�� ���� �� �ּž� ���� ���̿� ���� ������ ���� �� �ֽ��ϴ�.

���� �ڵ�� �޴����� paket modification �κ��� �����ؼ� ��������ϴ�.
'''


import pydivert

print("2014400021 HyoJun Shin")
print("http packet change : Michael => Gilbert")

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:
    for packet in w:
        if(packet.is_outbound): # ������ ��Ŷ
            payload = packet.tcp.payload
            #���⼭ get reqeust�� encoding �ɼ��� �ٲپ��ִµ� ù��° �ٸ����ε� ����� �������� Ȥ�� ���� �ι�° ����° �ٵ� �߰��� �־���.
            payload = payload.replace(b'Accept-Encoding: gzip', b'Accept-Encoding:     ')
            payload = payload.replace(b'Accept-Encoding: gzip,', b'Accept-Encoding:      ')
            payload = payload.replace(b'sdch', b'    ')
            packet.tcp.payload = payload
        if(packet.is_inbound): # ������ ��
            payload = packet.tcp.payload
            payload = payload.replace(b'Michael', b'Gilbert')
            packet.tcp.payload = payload
        w.send(packet, True) # ���⼭ �� ��° ���ڴ� �ٲ� ��Ŷ�� ���Ͽ� �ٽ� checksum�� ����ҰųĿ� ���� �ɼ�
