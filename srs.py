import serial
import time
import winsound
timer = 0.00
dummy='쪽쪽야옹'
goza = serial.Serial("COM1", 57600)
momiji = '|                                      ||                                      |'
oe = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'
nextline = '\n\r'
ong = '\a'
ro = '\r'
go = '\t'
onekey = '|'
noe = '\n'
oreo = oe + ro
up1 = b'\x8D'
up25 = b'\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D'
up27 = b'\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D'
up24 = b'\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D\x8D'
#txt = open('20720.txt',"r")
#for i in range(0, 25):
#    yaong = '\r' + txt.readline()
#    goza.write(yaong.encode('euc-kr'))
#goza.write(ong.encode('euc-kr')) # 삑!
#time.sleep(10)
#print('일어남')
#goza.write(ong.encode('euc-kr')) # 삑!
goza.write(up25)
goza.write(oreo.encode('euc-kr'))
txt1 = open('dummy1.txt',"r")
for i in range(0, 25):
    yaong = '\r' + txt1.readline()
    goza.write(yaong.encode('euc-kr'))
goza.write(up24)
goza.write(ro.encode('euc-kr')) #커서만 왼쪽으로 이동
#goza.write(ong.encode('euc-kr')) # 삑!
#time.sleep(10)
print('시작!')
winsound.PlaySound('still_jusik.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)
#goza.write(dummy.encode('euc-kr') + go.encode('euc-kr') + dummy.encode('euc-kr'))
#goza.write(oreo.encode('euc-kr'))
#goza.write(ro.encode('euc-kr')) #커서만 왼쪽으로 이동
#RI  Reverse Index (one line up) 8D

#김나성 구역
text1 = '랜덤 박스 시뮬레이션 실험:'
text2 = '피험자 반응'
goza.write(onekey.encode('euc-kr') + text1.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text2.encode('euc-kr'))
#time.sleep(6)
timer = timer + 6.00
print(timer)
text3 = '나왔다 병신들아!'
text4 = '안나왔다 병신들아!'
text5 = '나를봐'
text6 = '고고고빵 해도 안나왔다'
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text3.encode('euc-kr'))
#time.sleep(3.7)
timer = timer + 3.70
print(timer)
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text4.encode('euc-kr'))
#time.sleep(2.3)
timer = timer + 2.30
print(timer)
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text5.encode('euc-kr'))
#time.sleep(3)
timer = timer + 3.00
print(timer)
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text6.encode('euc-kr'))
#time.sleep(5.7)
timer = timer + 5.70
print(timer)
#똘3구역으로 넘어가는중
linereset = '                                      '
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr') + ro.encode('euc-kr') + onekey.encode('euc-kr'))


#똘3 1구역
text1 = '주식 거래소 현재 상황'
text2 = '대상:Jung Tae June'
goza.write(text1.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text2.encode('euc-kr') + nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr'))
#time.sleep(1.3)
timer = timer + 1.30
print(timer)
text3 = '정신병자야!'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text3.encode('euc-kr'))
#time.sleep(3.7)
timer = timer + 3.70
print(timer)
text4 = '야이 정신병자야!'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text4.encode('euc-kr'))
#time.sleep(1.9)
timer = timer + 1.90
print(timer)
text5 = '자신 있제'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text5.encode('euc-kr'))
#time.sleep(3.3)
timer = timer + 3.30
print(timer)
text6 = '오 심창치 않은데'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text6.encode('euc-kr'))
#time.sleep(3.3)
timer = timer + 3.30
print(timer)
text7 = '비트코인 망해요'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text7.encode('euc-kr'))
#time.sleep(2.2)
timer = timer + 2.20
print(timer) # 여기서 10줄, 여기까지 삭제 9줄 필요!
text8 = '주님 XXX야 속이 후련했냐!'
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text8.encode('euc-kr'))
#time.sleep(3.60)
timer = timer + 3.60
print(timer)
text9 = '모든것을 가져가야 후련했냐!'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text9.encode('euc-kr'))
#time.sleep(3.80)
timer = timer + 3.80
print(timer)
#time.sleep(5.0)

# 삭제 없이 2번째줄로 가야함!
goza.write(up1 + up1 + up1 + up1 + up1 + up1 + up1 + up1 + up1 + up1 + up1 + go.encode('euc-kr') + go.encode('euc-kr'))
text1 = '통신 채널 해킹'
back1 = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
text2 = '알수없는 통신:'
goza.write(onekey.encode('euc-kr') + text1.encode('euc-kr') + noe.encode('euc-kr') + back1.encode('euc-kr') + text2.encode('euc-kr'))
timer = timer + 0.60
print(timer)

text3 = '내가 사지말랬지'
text4 = '이 불신자들아'
back3 = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
goza.write(noe.encode('euc-kr') + back1.encode('euc-kr') + noe.encode('euc-kr') + noe.encode('euc-kr') + text3.encode('euc-kr'))

timer = timer + 2.00
print(timer)
goza.write(noe.encode('euc-kr') + back3.encode('euc-kr') + text4.encode('euc-kr'))
text5 = '신성모독하지마라'
text6 = '나 아니다'

timer = timer + 2.10
back4 = '\b\b\b\b\b\b\b\b\b\b\b\b\b'
print(timer)
goza.write(noe.encode('euc-kr') + noe.encode('euc-kr') + back4.encode('euc-kr') + text5.encode('euc-kr'))

timer = timer + 1.70
print(timer)
back5 = '\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b'
goza.write(noe.encode('euc-kr') + back5.encode('euc-kr') + text6.encode('euc-kr'))

timer = timer + 1.0
print(timer)

#똘3 2구역으로 넘어가는중
#txt1.close
#txt1 = open('dummy1.txt',"r")
#for i in range(0, 25):
#    yaong = '\r' + txt1.readline()
#    goza.write(yaong.encode('euc-kr'))
#goza.write(up24)
oe3 = '\n\n\n'
goza.write(oe3.encode('euc-kr') + ro.encode('euc-kr'))
for i in range(0, 11):
    goza.write(momiji.encode('euc-kr') + up1 + ro.encode('euc-kr'))
goza.write(momiji.encode('euc-kr') + ro.encode('euc-kr') + onekey.encode('euc-kr'))
text1 = '채널 복구중...'
text2 = '연결 재 설정...'
text3 = 'twitch.tv/jungtaejune 접속'
goza.write(ro.encode('euc-kr') + onekey.encode('euc-kr'))
goza.write(text1.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text2.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text3.encode('euc-kr') + nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr'))

#time.sleep(6.3)
timer = timer + 6.3
print(timer)
text4 = '난 화난게 아냐'
goza.write(text4.encode('euc-kr'))
#time.sleep(4.25)
timer = timer + 4.25
print(timer)
text5 = '나는 도네로 벌었어'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text5.encode('euc-kr'))
#time.sleep(5.0)
timer = timer + 5.0
print(timer)
text6 = '니들은 주식하지마라'
text7 = '제발...'
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text6.encode('euc-kr'))
#time.sleep(4.0)
timer = timer + 4.0
print(timer)
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text7.encode('euc-kr'))
#time.sleep(2.85)
timer = timer + 2.85
print(timer)
text8 = '부탁이야 내가'
text9 = '그돈으로 치킨 사먹어'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text8.encode('euc-kr'))
#time.sleep(4.0)
timer = timer + 4.0
print(timer)
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text9.encode('euc-kr'))
#time.sleep(4.8)
timer = timer + 4.8
print(timer)
text10 = '화려한 인생보다 x되지 않는 인생'
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text10.encode('euc-kr'))
#time.sleep(5.4)
timer = timer + 5.4
print(timer)
text11 = '쉽게 벌어봐야 결국 다없어져'
goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text11.encode('euc-kr'))
#time.sleep(4.3)
timer = timer + 4.3
print(timer)
text12 = '버는 동안 재밌으면 그게 좋지'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text12.encode('euc-kr'))
#time.sleep(4)
timer = timer + 4
print(timer)
text13 = '주식방송하고 게임방송도하고'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text13.encode('euc-kr'))
#time.sleep(4)
timer = timer + 4
print(timer)
text14 = '지금 이대로가 젤 좋아'
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text14.encode('euc-kr'))
#time.sleep(3.5)
timer = timer + 3.5


#똘3 4구역으로 넘어가는중
linereset = '                                      '
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
for i in range(0, 16):
    goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr') + ro.encode('euc-kr') + nextline.encode('euc-kr')+ nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr'))
text1 = '추신:'
goza.write(text1.encode('euc-kr'))

#똘3 4구역
text2 = '주님이 전화해도'
text3 = '붓다가 방송봐도'
text4 = '광림이 내려와도'
text5 = '우리로 올라와도'
text_no = '하지마'

goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text2.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text_no.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text3.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text_no.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text4.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text_no.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text5.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + text_no.encode('euc-kr'))

goza.write(nextline.encode('euc-kr') + nextline.encode('euc-kr') + onekey.encode('euc-kr') + text_no.encode('euc-kr'))

linereset = '                                      '
goza.write(nextline.encode('euc-kr') + onekey.encode('euc-kr') + ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
for i in range(0, 16):
    goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr'))
goza.write(ro.encode('euc-kr') + up1 + onekey.encode('euc-kr') + linereset.encode('euc-kr') + ro.encode('euc-kr') + onekey.encode('euc-kr'))