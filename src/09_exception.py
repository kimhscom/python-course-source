# 09_exception.py

'''
    예외처리
        - 의도치 않은 오류 발생에 대한 처리
            > 오류 발생 : 프로그램 중단 후 오류 메세지 출력

        try, except문 제공!

try :
    기본 수행문
except :
    오류 발생 시 수행문
'''

# (1) 예외처리 기본
'''
try :
    # 아무 조건없이 진입 <오류가 발생할 지도 모르는 코드들을 작성>
    num = int( input("숫자 입력 : ") ) # 오류 발생 시점에 바로 except로 점프!
    print("입력한 숫자 :", num)
    # 오류가 발생하지 않으면 except는 수행되지 않는다.
except :
    print("숫자를 입력하세요!!")

print("프로그램 종료")
'''


# (2) finally : 예외처리 문법에 속하며, 마지막에 무조건 수행되는 구간

# 모든 프로그래밍 언어에서는 어떤 수를 0으로 나누면 오류가 발생!!
'''
try :
    num = int( input("나눌 숫자 입력 : ") )
    print( "나눈 결과 :", (10/num) )
except :
    print("0으로 나눌 수 없습니다!")
finally :
    # 오류 발생 여부와 상관 없이 수행된다.
    print("예외처리 구간 종료!")
'''


# (3) 오류 원인에 따라 나누어 예외처리 
'''
try :
    num = int( input("나눌 숫자 입력 : ") )
    print( "나눈 결과 :", (10/num) )

    my_list = [1,2,3] # 요소 3개 (0,1,2,-1,-2,-3)
    print( "my_list[{}] = {}".format( num, my_list[num] ) )

    print(zzzzz) # 없는 변수라서 여기선 무조건 오류!
    # (1) 인덱스 범위 초과 -> "인덱스 범위가 잘못되었습니다!"
    # (2) 없는 변수        -> "이름이 잘못되었습니다!"
    
except ZeroDivisionError : # 마치 if문의 조건처럼, 오류 명칭을 사용!
    print("0으로 나눌 수 없습니다!")
except ValueError : # 발생한 오류에 알맞은 except로 진입 (순서대로 찾음)
    print("숫자를 입력하세요!")
except NameError :
    print("이름이 잘못되었습니다!")
except : # 위에서 걸러지지 않은 모든 오류를 처리! (마치 else처럼)
    print("뭔진 모르겠지만 오류가 발생하긴 했다!!")
'''


# 07_repetitive_while.py 의 연습문제 6번 - 숫자맞추기 코드를 여기에 붙여넣기
#  > 아직 완성 안 된 분들은 지금 완성하면서 하세요!

# 사용자가 숫자를 입력하지 않았다면, "숫자를 입력하세요!" 라고 출력 후 다시 입력 받기
#  > 이때 입력한 것은 횟수에 카운팅하지 않는다.
#  > 모든 코드를 try/except로 처리하지 말고, '오류 발생하는 코드'만 try로 처리

import random
answer = random.randint(1, 100) # 1~100 정수 중 랜덤으로 1개 추출
print("게임 관리자용 정답 공개 :", answer)
# 해야할 일 : 입력받기, 비교하기, 횟수카운팅

# 반복문으로 정답을 맞출 때까지 수행
# 무얼 수행? -> 입력, 비교, 카운팅
# 정답숫자 만드는걸 반복한다? --> 계속 정답이 바뀌기 때문에.. 1/100 확률로 맞춰야함;;;

count = 0

while True : # 무한반복 + break 형태
    # 1. 입력받기
    try :
        num = int( input("정답 숫자 입력 : ") )
        count += 1 # 입력을 했다 = 횟수 1증가
    
    # 2. 비교하기
        if num == answer : # 정답이면,
            print("정답입니다!! {}회 만에 성공!".format(count))
            break

    # if에서 break를 했기 때문에, 코드가 이 아래로 내려온다면, 무조건 정답이 아니라는 얘기!

        if num > answer : # 정답보다 입력숫자가 크면,
            print("더 작은 수를 입력해보세요.")
        else : # 무조건 작다임
            print("더 큰 수를 입력해보세요.")

    except ValueError :
        print("숫자를 입력하세요!")
