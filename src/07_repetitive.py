# 07_repetitive.py

'''
    [반복문]
        조건에 만족하면 수행한다. (조건문과 동일)
            > 단, 조건에 만족하지 않을때까지....

        1. while문
            - 조건식이 참이면 수행문 수행
            - if문과 기본 구조가 동일
                > if문 : 조건이 참이면 수행하고 끝
                > while문 : 조건이 참이면 수행하고 다시 조건식을 비교

[while문 기본 구조]
while 조건식 :
    수행문
    수행문
    
        2. for문
            - 리스트, 튜플, 문자열 등 요소가 나열된 형태의 값을
              첫 요소부터 마지막 요소까지 변수에 대입하며 반복

[for문 기본 구조]
for 변수 in 리스트 (또는 문자열 등) :
    수행문
    수행문
            

        * 반복문 공통
            - break문 : 반복문을 빠져나간다 (탈출)

            - continue문 : 반복문의 첫 문장으로 돌아간다
                           수행문을 끝낸다.
                    while문 : 조건식으로 돌아가서 조건식 비교
                    for문 : 다음 요소를 대입하러 돌아간다.
'''
'''
print("[whilie문]")

num = 0

while num < 3 :
    #pass # 수행문에 아무것도 쓰고 싶지 않을 때 사용
    print( "num = {}".format(num) )
    num += 1 # num의 값에 1을 더한 뒤 num에 다시 대입 (누적)

# num이 2를 출력하고, 3이 된 뒤 조건식이 만족하지 않아서 끝났다.
print("이때 num의 값은? ", num)

# 무한반복 탈출 : Ctrl + C
'''

'''
조건식에 들어가는 변수는 '조건변수'
반복문에서는 조건변수를 다루는게 매우 중요하다.
 > 반복 횟수 등이 달라짐

조건변수 초기값(생성)
while 조건식 :
    수행문 (반복 수행할 코드 + 조건변수 변화식)
'''

# while문은 처음엔 조건식 만족시켜야 수행한다.
# > 언젠가는 만족하지 않도록 코드를 작성 (탈출 조건)

'''
# 반복 횟수 지정
count = int(input("반복 횟수 입력 : "))

import time # time 모듈 (시간과 관련된 기능들 사용 가능)

while count > 0  :
    print("카운트다운 : {}!!".format(count) )
    count -= 1
    time.sleep(1) # 코드가 여기서 잔다.(대기) - second
'''


# 특정 조건 만족
# num = int( input("9를 입력하면 종료합니다 : ") )
'''
num = 0 # 초기값을 9만 아닌 값으로 하면, 일단 조건식을 만족한다.
while num != 9 :
    num = int( input("9를 입력하면 종료합니다 : ") )
'''

# break 사용
'''
while True : # 무한반복 조건
    num = int( input("9를 입력하면 종료합니다 : ") )
    if num == 9 :
        break
'''
# while문은 일반적으로 무한반복+break 형태로 사용
# > 조건이 까다롭거나 복잡할 때, if문으로 대체하여 탈출하는게 편하다.


# countinue 사용
'''
num = 1

while num < 11 :
    if num % 2 == 0 : # 2의 배수 (짝수)
        num += 1
        continue # 더이상 수행문을 수행하지 않고, 조건식으로 '점프'
        # 반복문의 수행문이 끝나는 '새로운 지점'을 만든 것!

    print(num)
    num += 1
    # 수행문이 끝나는 '원래 지점'
'''

# break, continue는 '반복문' 안에서만 사용 가능한 명령인데... if문 안에 사용했다?!
# if문 없이 사용하는
# break    : 1회 수행 때 무조건 반복문이 끝난다. (반복문을 사용할 이유가 없어짐)
# continue : 무조건 조건식으로 돌아간다. (이 아래 쓰여진 수행문은 절대 수행 X)

print()
print("[for문]")

# z는 만들어둔 변수는 아니지만, for문에서 '대입'되면서 만들어진다.
# i, while문의 '조건식'에 사용되는 변수와는 다르다.
for z in [1,2,3] :
    print(z)

print(z) # 마지막에 대입됐던 값을 유지한채 계속 사용할 수 있다.


print()

for z in ["한국", "미국", "중국"] :
    # 요소 단위로 대입된다. (요소를 하나씩 인덱싱하다)
    print(z + " : " + z[0]) # z는 문자열!

print()

for z in "123abc" :
    print(z)

print()

for z in [1,2,3] :
    print("하하하하하하하하")

# 꼭 z를 사용해야만 하는건 아니다!
print(z) # 그래도 마지막 요소 값인 3이 대입!
print()


# range() : 지정한 범위 만큼의 정수를 반환
for i in range(5) :
    print(i)

'''
    range(5)     : 0~4
    range(10)    : 0~9
    range(1, 10) : 1~9
        > 마치 슬라이싱과 비슷하다! (끝나는 값은 포함되지 않는다.)

    range(1, 10, 2)     : 1~9, 2씩 증가 -> (1,3,5,7,9)
    range(1, 10, -1)    : 10~1, 1씩 감소
    reversed(range(10)) : 0~9 -> 9~0
'''
print()

# for문으로 1~10 합 구하기
'''
my_sum = 0
for i in range(1, 10+1) :
    my_sum += i
print("합 :", my_sum)
'''

# 입력 횟수만큼 반복
'''
count = int(input("반복 횟수 입력 : "))
#for i in range(count, 0, -1) :
for i in reversed(range(1, count+1)) :
    print("카운트다운 {}!!".format(i))

print()
'''

# for문 활용 예시 (1)
guest_list = [["홍길동", 21], ["이몽룡", 23], ["성춘향", 17], ["임꺽정", 19], ["김철수", 35]]
# 손님 1명에 대한 정보(요소)를 리스트로 지니고 있다.
# 손님 1명에 대한 정보는 '문자열',정수 이다. (이름,나이)

count = 0 # 몇 번째 입장 손님인지!

for guest in guest_list :
    #print(guest) # 대입된 값은 리스트이다!!

    # name, age는 반복할 때마다 계속 바뀐다. (guest에 대입되는 요소가 달라지니까~~)
    name = guest[0]
    age  = guest[1]
    count += 1

    print("{}번 손님~~ 입장하세요!".format(count))

    # 조건문 1    
    if age > 19 :
        print("{}님은 성인입니다. 입장해서 마음껏 노세요~~".format(name))
    else :
        print("{}님은 미성년자입니다. 입장하면 우유만 드세요~~".format(name))

    # 조건문 2
    if age < 20 :
        continue # 미성년자는 여기서 수행문이 끝!

    print("성인은 보드카 한잔 서비스~~")

print()

# for문 활용 예시 (2)
# 반복문도 수행문 안에 또 다른 반복문을 넣어서 '중첩' 시킬 수 있다.

print("i j")
print("---")

# 2중 for문
for i in range(3) : # 0~2
    for j in range(3) : # 0~2
        print(i,j)

    print("나는 몇 번 출력될까요?")
    # i의 for문 수행문 '끝'

print()

print("3중 for문 - 이렇게 하지 말기")
for i in range(3) :
    for j in range(3) :
        print("ㅋ") # 9회
        for k in range(3) :
            print(i,j,k)
        print("ㅎ") # 9회
    print("ㅠㅠ") # 3회

# for문(반복문)이 3회 이상 중첩되면, 코드 읽기가 상당히 까다롭다.
# > 유지보수 측면에서도 좋지 않다.

print()

# 중첩된 반복문은 왜 사용할까?
# 반복할 때마다 변하는 값이 2개 이상일 때, 다루면 좀 편하다.

# 2중 for문 - 구구단(단, 곱)

for i in range(2,9+1) : # 단 (2~9)
    # i가 2일 때,아래 for문을 9회 수행하여야 2단이 끝!, 그 다음 대입되면 3단
    for j in range(1, 9+1) : # 곱(1~9)
        # j는 1~9까지 곱해지는 숫자
        print("{} * {} = {}".format(i,j,(i*j)))

    print("<{}단 끝!>".format(i))

# 구구단의 출력은 총 72회이다. (8개의 단, 각 단마다 9회씩 =72)
# 단은 9회 마다 1씩 증가
# 곱은 1부터 계속 1씩 증가하다가, 9회를 출력하면 다시 1로 변경
# > 이 원리를 이용하면 for문 1개로도 구구단을 출력할 수 있다! (연습문제)
