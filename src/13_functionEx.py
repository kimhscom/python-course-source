# 13_functionEx.py

# 파이썬에서 함수를 나누는 용어
#   내장함수 : print, int, input과 같이 그냥 바로 사용 가능한 함수들
#   외장함수 : random, sys 등 모듈을 import해야 사용 가능한 함수들

import random as r

print( r.randint(1, 100) )

for i in range(10) :
    if r.randint(1,2) == 1 :
        print("절반의 확률!")

my_list = ["가위", "바위", "보"]
print( r.choice(my_list) ) # choice() : 전체 요소 중 하나를 랜덤으로 '반환' (인덱싱)

# 1. 덧셈 맞추기 게임
'''
num1 = r.randint(1,50)
num2 = r.randint(1,50)

input_num = int( input( "{} + {} = ".format(num1,num2) ) )

if input_num == num1+num2 :
    print("정답!")
else :
    print("오답!")
'''


# 응용
#   1. 난이도 - 사칙연산, 문제 숫자의 범위
#   2. 점수
#   3. 반복 횟수 (문제 개수)


# 2. 가위바위보 게임
'''
my_list = ["가위", "바위", "보"]
com = r.choice(my_list)
user = input("가위~ 바위~ 보!! : ")

print( "com vs user" )
print( "{} vs {}".format(com, user) )

# 승패 판별
if com == user :
    print("비겼다!")
else :
    if com == "가위" and user == "보" :
        print("졌다..")
    elif com == "가위" and user == "바위" :
        print("이겼다~~!")
    # 너무 길어서 이하 생략..
'''

# 응용
#   1. 반복
#   2. 점수
#   3. 묵찌빠 (심화)


# 3. 지난 시간 맞추기
import time   # 시간 관련된 기능이 있는 모듈
#print( time.time() ) # time() : 1970-01-01 00:00:00 기준으로 현재까지 지난 시간을 초단위

input("엔터를 누르고 5초를 마음속으로 셉니다.")
start_t = time.time()

input("정확히 5초를 세면 엔터를 누르세요!!")
end_t = time.time()

t = end_t - start_t
print( "실제 경과 시간 : {:.2f}초".format(t) )
print( "차이 : {:.2f}초".format( abs(5-t) ) ) # abs() 절대값으로 반환 (양수)

