# -*- coding: cp949 -*-
'''
BOB에서는 C 언어로 짜 보았으니 이번에는 python으로 구현해 보았습니다.
pydivert는 windivert를 쉽게 사용할 수 있게 만드는 python package이고
https://github.com/ffalcinelli/pydivert에 메뉴얼이 있긴 하지만 실제로 package 설치는
pip install pydivert를 통해 해 주셔야 버전 차이에 의한 에러를 피할 수 있습니다.

다음 코드는 메뉴얼의 paket modification 부분을 참조해서 만들었습니다.
'''


import pydivert

print("2014400021 HyoJun Shin")
print("http packet change : Michael => Gilbert")

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:
    for packet in w:
        if(packet.is_outbound): # 나가는 패킷
            payload = packet.tcp.payload
            #여기서 get reqeust의 encoding 옵션을 바꾸어주는데 첫번째 줄만으로도 충분해 보이지만 혹시 몰라 두번째 세번째 줄도 추가해 주었다.
            payload = payload.replace(b'Accept-Encoding: gzip', b'Accept-Encoding:     ')
            payload = payload.replace(b'Accept-Encoding: gzip,', b'Accept-Encoding:      ')
            payload = payload.replace(b'sdch', b'    ')
            packet.tcp.payload = payload
        if(packet.is_inbound): # 들어오는 패
            payload = packet.tcp.payload
            payload = payload.replace(b'Michael', b'Gilbert')
            packet.tcp.payload = payload
        w.send(packet, True) # 여기서 두 번째 인자는 바꾼 패킷에 대하여 다시 checksum을 계산할거냐에 대한 옵션
