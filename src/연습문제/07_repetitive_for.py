# for문 연습
# n의 배수 : 어떤 숫자를 n으로 나눈 나머지가 0   --> num % n == 0 --> num은 n의배수
# 공배수 :    n1과 n2의 공배수 = 둘 다 만족!    num % n1 == 0 and num % n2 == 0
'''
    1. 1부터 입력 받은 수까지 '짝수'의 합 구하기

        [출력결과]
        5
        1~5까지 짝수의 합은 6입니다.
'''
'''
total = 0

num = int(input("숫자 입력 : "))

for i in range(1, num) :
    if i % 2 == 0 :
        total += i

print("1~{}까지 짝수의 합은 {}입니다.".format(num, total))
'''


'''
    2. 1부터 200까지 3과 4의 공배수를 하나의 변수에 '누적'
       누적된 수가 1000을 초과하면 반복문을 '탈출'
       이때, 누적된 수와 마지막에 더했던 공배수를 출력

        [출력결과]
        누적된 수 : 1092
        더한 수 : 156
'''
'''
total = 0

for i in range(1, 200) :
    if i % 3 == 0 and i % 4 == 0 :
        total += i

    if total > 1000 :
        break

print("누적된 수 : {}".format(total))
print("더한 수 : {}".format(i))        
'''


'''
    3. 1~100 사이 정수 중, 3의 배수와 5의 배수를 '역순'으로 출력
       단, 3과 5의 공배수는 <15> 처럼 출력

       [출력결과]
       100 99 96 95 93 <90> 87 ... 5 3

'''
'''
for i in reversed(range(1, 100+1)) :
    if i % 3 == 0 and i % 5 == 0 :
        print("<{}>".format(i))
        continue
    print("{}".format(i))
'''


'''
    난이도 <상>
    4. 2중for문 구구단 예제를 for문 1개만 사용해서 만들어보기
        - 총 반복 횟수 = 72회
        - 처음 단은 2
        - 곱해지는 숫자는 처음이 1
        - 9회 수행마다, 단이 1 증가, 곱해지는 숫자는 1로 변경
'''

i = 2
j = 1

for total in range(72) :
    if j == 10 :
        j = 1
        i += 1
        print()
    print("{} * {} = {}".format(i, j, (i*j)))
    j += 1


        








