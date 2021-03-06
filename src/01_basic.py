1+1 #1+1 덧셈 연산만 하고 결과를 출력하지 않았다.
print(2+2) # 2+2 덧셈 연산의 결과를 print 명령으로 출력했다.

# 대화형 shell 에선 print 명령을 사용하지 않아도 결과가 나온다.
# 하지만 shell 에 작성한 내용은 저장되지 않기 때문에, 우린 소스코드에 작성

'''
주석(comment)
    1. 소스 코드에'설명'을 추가하는것
    2. 실행 시 무시된다. 프로그램 수행에 영향이 없다.
    3. 한 줄 주석 # 뒤부터 주석처리
    4. 여러 줄 주석 ''' ''' 또는 """ """ 로 묶는다.

print() 함수
    1. 화면으로 데이터(값)를 출력하는 함수
        > 함수 : '특정 행위'를 하기 위해 미리 만들어 놓은 '기능'
        > 화면 : IDLE(shell)이나 콘솔(cmd)창

문자열 (string)
    - 하나 하나의 문자들이 나열되어 합쳐진 '하나의 값'
    - 문자열을 만드려면 'abc' 또는 "abc" 처럼 따옴표로 묶는다.
        > (참고) 다른 언어에서는 큰 따옴표만 문자열로 인정된다.

'''
print("안녕")
print('안녕')
# 짝을 맞춰야 한다!

# 오류! 라고 주석이 있는 코드는 맨 앞에 반드시 주석처리를 한다!
# print(안녕) 오류! -->인식할 수 없는 코드 (문자열이 아니다)

# print() 함수는 미리 익숙해져야한다. --> 결과를 확인할 수 있는 가장 빠른 방법

# 여러 값 출력의 기본 : 콤마(,)로 나열한다.
print(1,2,3) # 정수 3개를 나열하여 각각 출력

# 파이썬은 기본이 한 줄에 하나의 명령을 수행
# 한 줄에서 여러 명령을 사용하고 싶을 때 세미콜론(;) 사용

print("a","b")
print("A","B")

'''
    print() 함수에서 기본으로 사용되는 '구분기호'와 '마지막 기호'
        (1) 콤마(,)로 값을 구분할 때 기본으로 '공백'이 적용
            sep=' '
        (2) print() 의 출력이 끝나면 기본으로 '개행'이 적용 (줄바꿈)
            end='\n'
            \n은 개행을 하는 특수한 문자(이스케이프 문자)
            문자열 안에서만 효력이 있다.

        --> 우리가 직접 명시해서 입맛대로 바꿀 수 있다!

'''
print(1,2,3)
print(1,2,3,sep='') # 공백 대신 '빈 문자열'을 적용

print("안녕",end='') # 개행 대신 '빈 문자열'을 적용
print("하세요")

print(1,2,3,sep='ㅋㅋ',end='ㅎㅎ')
print(4,5,6) #위에서 개행하지 않았기 때문에 4 5 6은 붙어서 나온다!

print() # 출력할 값은 없지만 개행만 적용! 내용 분리 용도로 자주 사용할 예정

# 덧셈 기호 (+)의 사용
print( 1 + 1 ) # 숫자+숫자=덧셈 연산
print( "1" + "1" ) # 문자열 + 문자열 = 문자 연결
print( "1"   "1" ) # 이렇게는 사용하지 않는다.

#print( "1" + 1 ) # 오류! 문자+숫자=오류
# 덧셈은 같은 성질의 값끼리만 덧셈이 가능
# (참고) JAVA 언어에서는 숫자가 글자 취급되어 '연결'이 된다.

print( "1", 1 )
# print()에서 출력 시 어떤 형태의 값이던지 나열할 수 있다. (연산 x)
# 어떤 형태? 자료형(data type) 배울 예정
print(2018, "년도 입니다.", sep="")

# [중요]
# '연산' 이라는 행위를 하면, 새로운 값을 만들어 낸다.
print()

'''
    변수 (variable)
        - 기본 정의 : '하나의 값'을 저장하는 메모리 공간
            > 메모리 : 프로그램 수행 시 사용되는 기억 장치(RAM)
        - 파이썬에서 변수는 '객체'를 가리킨다.
'''

# 프로그래밍 언어에서 등호(=)는 '같다'가 아닌 '대입'의 개념
# > 우측의 값을 좌측 공간에 대입한다.

# 파이썬에서는 변수를 '선언' 할 때 자료형의 타입을 따로 명시할 필요 없다.
# (참고) C,JAVA 등에서 int a = 10 , string b = "문자" 이런 식으로 명시
a = 1
print(a)
a = "안녕~~!" # a 변수는 기존에 정수1을 가리키던 연결 고리가 끊어진다.
print(a)

# 변수에 값 대입 (1) - 하나씩
a = 1
b = 2
c = 3
print(a, b, c)

# 변수에 값 대입 (2) - 한 번에 (유용)
a, b, c = 4, 5, 6 # 짝을 맞춰줘야 한다.
print(a, b, c)

# 변수에 값 대입 (3) - 모두 같은 값
a = b = c = 7
print(a, b, c)

# 변수에 값 대입 (4) - 1과 동일 (명령 3개를 한 줄에)
a = 8; b = 9; c = 10
print(a, b, c)

# 강사가 추천하는건 (1)번. 좌우로 왔다갔다 하면서 읽지 않는다.
print()

# 변수가 값을 가리킨다?
a = 3
b = 3
print( id(3) ) # id() 함수 : 값의 고유한 id를 가르쳐준다.
print( id(a) )
print( id(b) )

# 참조하는(가리키는) 개수 확인하기
import sys   # sys 라는 이름의 '모듈'을 이 순간부터 사용하겠다!

print( "처음 정수2018 :", sys.getrefcount(2018) )
# get : 구하겠다
# ref : reference 참조하는
# count : 개수
# >> 정수 2018 값을 참조하는 개수를 구하겠다

# 값이 2가 나왔다 = 아무데서도 사용하고 있지 않다.
# 그럼 왜 2? getrefcount()가 확인하려고 하는 시점에 사용이 됐다.
# 2는 최소 값

a = 2018
print( "a에 대입 후 :", sys.getrefcount(2018) )
b = 2018
print( "b에 대입 후 :", sys.getrefcount(2018) )

del(a) # 변수를 제거하는 명령어
del(b)

print( "a, b 제거 후 :", sys.getrefcount(2018) )

#print(a) # 오류! 제거된 변수

'''
    변수명
        1. 한글 가능! 하지만, 영어로 한다. (파이썬 기본이 영어)
        2. 기호는 _ 만 사용
        3. 숫자 가능! 하지만 첫 글자로는 안 된다.
        4. 대소문자 구분 (중요)
            - 프로그래밍 언어에서는 모든 곳에서 대소문자가 구분된다.
            - 알파벳 대소문자는 '값' 자체가 다른 문자
        5. 파이썬에서 이미 사용하고 있는 '예약어' 사용 불가
            - import, del 등 노란색 명령어 : 키워드 (사용 불가능)
            - print, id 등 보라색 : 내장함수 (사용은 가능)

            > 색깔있는 단어는 사용하지 않기

        * 변수 이름을 지을 때 (작명) '의미'를 부여한다.
            > 명사가 들어간다.
            > 하다못해 최소한의 의미라도 부여
                숫자면 num1, num2
                문자면 str1, str2

'''
print()
print("재미있는 파이썬~~!")
print = "정말인가요?" # 변수 선언
#import = "하하하" # 오류! 실행도 안 됨. 문법 오류

#print("네~~재밌어요!!") # 오류! print 이름은 현재 '문자열' (str)
del(print) # 변수화된 print 제거
print("넵~~ ㅎㅎㅎ") # 원래의 함수 기능을 찾았다!

# 파이썬에서 이미 사용하는 있는 예약어(키워드) 목록 확인
import keyword
print( keyword.kwlist ) # key word list (키워드 목록)
