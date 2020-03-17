# 함수 연습
'''
    1. 홀짝 판별기
        함수의 순기능 : 전달된 숫자가 홀수인지 짝수인지 판별
            > 짝수 : Even Number
            > 반환 값이 있는 형태와 없는 형태로 함수를 2개 만들기
            > 0은 "0입니다"

          1. 숫자 입력
          2. 입력 받은 숫자를 함수의 매개변수로 전달
          3. 함수는 전달 받은 매개변수의 값으로 홀짝 판별

        [출력결과]
        숫자 입력 : 20
        함수1 : 짝수입니다.
        함수2 : 짝수입니다.
'''
'''
number = int(input("숫자 입력 : "))

def Even1(num) :
    if num % 2 == 0 :
        return print("함수1 : 짝수입니다.")
    else :
        return print("함수1 : 홀수입니다.")

def Even2(num) :
    if num % 2 == 0 :
        print("함수2 : 짝수입니다.")
    else :
        print("함수2 : 홀수입니다.")

Even1(number)
Even2(number)
'''


'''
    2. 두 수를 입력 받고, 큰 수에서 작은 수를 뺀 결과 값을 '반환'하는 함수 정의
        - 계산기 : calc
        - 위 내용이 함수의 순기능임
         > 매개변수 2개, 반환 값 있음

        [출력결과]
        두 수 입력 : 1 20
        결과 : 19
'''
'''
num1, num2 = map(int, input("두 수 입력 : ").split())

def calc(a, b) :
    if a > b :
        return print("결과 : {}".format(a-b))

    elif a < b :
        return print("결과 : {}".format(b-a))

    else :
        print("두 수가 같다.")

calc(num1, num2)
'''


'''
    3. 1~10 사이의 두 수를 입력 받기
       1~100까지 전달된 두 수의 공배수를 출력하는 함수만들기 (반환 X)
        > 매개변수 2개, 반환 값 없음

           [출력결과]
           두 수 입력 : 3 5
           결과 : 15 30 45 60 75 90
'''
'''
num1, num2 = map(int, input("두 수 입력 : ").split())

def common(a, b) :
    print("결과 : ", end='')
    for i in range(1, 100+1) :
        if i % a == 0 and i % b == 0 :
            print(i, end=' ')
            
common(num1, num2)
'''

'''
    4. 소수 출력하기
        1부터 입력 받은 수까지 소수(PrimeNumber)만 출력하기
            > 소수 : 1과 나 자기자신 숫자로만 나누어떨어지는 수
                11 = 소수
                10 = 소수 아님 (2,5로도 나누어떨어짐)

        함수의 순기능 : 전달된 1개의 숫자가 소수인지 아닌지 판별하여 반환
            소수이면 True 반환
            소수가 아니면 False 반환
                is_prime_number(11) 호출하면 반환 값은 True
                is_prime_number(10) 호출하면 반환 값은 False

            > 1은 소수가 아님
            
        [출력결과]
        숫자 입력 : 20
        소수 : 2 3 5 7 11 13 17 19
'''
'''
num = int(input("숫자 입력 : "))

def is_prime_number(i) :
    for num in range(2, i) :
        if i % num == 0 :
            return False
    return True
    
print("소수 : ", end='')

for number in range(2, num+1) :
    if is_prime_number(number) :
        print("{}".format(number), end=' ')
'''


'''
    5. 재귀함수로 팩토리얼 값 구하기
        팩토리얼(factorial) : 1부터 어떤 수까지 모두 곱한 결과
            5! = 5 * 4 * 3 * 2 * 1
               = 5 * 4!
            3! = 3 * 2 * 1
               = 3 * 2!
            2! = 2 * 1!
            1! = 1

            n! = n * (n-1)!

        [출력결과]
        숫자 입력 : 5
        5! = 120
'''

num = int(input("숫자 입력 : "))

def fac(i) :
    if i == 0 :
        return 1
    return i * fac(i-1)

print("{}! = {}".format(num, fac(num)))








