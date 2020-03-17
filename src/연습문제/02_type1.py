'''
    1. 문자열 출력 연습
        - 출력결과를 아래 2가지 방법으로 출력하기 (출력결과가 2번 출력돼야함)
            (1) 작은따옴표 3개 - 이스케이프 문자 사용 X
            (2) 큰따옴표 1개  - 이스케이프 문자 사용 O

        - print()는 각각 1번만 사용 (총 2번)

[출력결과]
철수 "안녕? 파이썬 재밌지?"
영희 "응, 너무 재밌어!"
'''

# 1. 작은따옴표 3개
# 철수 ~~
# 영희 ~~
print('''철수 \"안녕? 파이썬 재밌지?\"
      영희 \"응, 너무 재밌어!\"''') 

# 2. 큰따옴표 1개
# 철수 ~~
# 영희 ~~
print("철수 \"안녕? 파이썬 재밌지?\"\n영희 \"응, 너무 재밌어!\"")

'''
    2. 문자열 연산 연습             -> 어려울 수 있으니 마지막에 하세요.
        - print() 3번만 사용
        - 연산 : 덧셈, 곱셈
            곱셈 : * , 공백 ' '*5, 파이썬최고
            hint : 연산=하나의 값을 만듦 ==> ( ) 소괄호로 묶는다.

[출력결과]
********************       별 20개
     파이썬최고             파이썬최고 앞에 빈칸 5개
     파이썬최고             파이썬최고 앞에 빈칸 5개
     파이썬최고             파이썬최고 앞에 빈칸 5개
********************       별 20개
'''

print("*" * 20)  # 별 20개 출력

print( (" "* 5 + "파이썬최고\n") *3, end='')  # 별 안쪽에 들어갈 3줄 출력

print("*" * 20)  # 별 20개 출력

'''
    3. 문자열 슬라이싱 연습
        - phone_number 에서 숫자만 가져와서 새로운 변수에 저장
'''

phone_number = "010-8383-9133"
only_number = phone_number[0:] # "?" 지우고, 슬라이싱 하기
print(only_number) # 01083839133

'''
    4. 문자열 슬라이싱 연습
        - info 에서 이름과 성별을 각각 변수에 저장
'''

info = "한수창 - 남자"
name = info[:4] #  "?" 지우고, 슬라이싱 하기
gender = info[-2:] # "?" 지우고, 슬라이싱 하기
print(name)   # 한수창
print(gender) # 남자

'''
    5. 문자열 포매팅 연습
        - 아래 3개의 변수를 미리 만들어 놓고, 포매팅을 사용하여 출력
        
name  = "한수창"
age   = "20"
phone = "010-8383-9133"
        
        (1) "".format 사용
        (2) 포매팅 사용하지 않고 출력 -> 아마도 제일 복잡한..^^;
        
[출력결과]
이름 : 한수창
나이 : 20
전화 : 010-8383-9133

'''

name = "한수창"
age = 20
phone = "010-8383-9133"

# (1) "".format 사용
print("이름 : {}".format(name))
print("나이 : {}".format(age))
print("전화 : {}".format(phone))

# (2) 포매팅 사용하지 않고 출력
print("이름 : " + str(name))
print("나이 : ", age, sep='')
print("전화 : " + str(phone))

'''
    6. 문자열 포매팅 연습
        - 문자열.format() 을 이용하여 20칸 크기 확보 후 가운데 정렬! (방식 자유)
        - 문자열 곱셈 연산은 사용하지 않기

[출력결과]
====================
       String
====================


'''
print("{:=^20}".format("="))
print("{:^20}".format("String"))
print("{:=^20}".format("="))
