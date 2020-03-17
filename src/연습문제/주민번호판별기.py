# 주민번호판별기.py
'''
    주민등록번호 진위 판별기
        1. 생년월일 유효성 검사
            월 : 1~12
            일 : 1~31  (월에 따라 다르다.)
            윤년은 아래 둘 중 하나를 만족해야 한다. (윤년이면 2월은 29일까지)
                1) 4의 배수이면서 100의 배수가 아님
                2) 400의 배수이다

        2. 성별 검사
            1,2 : 1900년대 남/녀
            3,4 : 2000년대 남/녀
            5,6 : 1900년대 외국인
            7,8 : 2000년대 외국인
            9,0 : 1800년대 남/녀

        3. 유효성 검사
            인터넷에서 '주민등록번호 유효성 검사' 검색하면 나옴!
            각 자리수를 2,3,4,5,6,7,8,9,2,3,4,5 와 곱한 결과를 더하고 (12개)
            11로 나눈 나머지에서 11을 뺀 숫자가 마지막 숫자와 일치해야 정상!


        입력 규칙 : 010101-1111111   형태로 - 포함
'''
while True :
    jumin = input("주민번호 입력 : ")
    if jumin == "-1" :
        print("프로그램을 종료합니다.")
        break

    # 판별구간
    if len(jumin) != 14 :
        print("다시 입력!!")
        continue

    # 생년월일 유효성 검사
    year = jumin[0:2]
    month = jumin[2:4]
    day = jumin[4:6]

    # 성별 검사
    if jumin[7] == '1' or jumin[7] == '3' or jumin[7] == '9' :
        sex = '남자'
    elif jumin[7] == jumin[7] == '2' or jumin[7] == '4' or jumin[7] == '0' :
        sex = '여자'
    else :
        sex = '외국인'

    print("{}".format(sex))


'''
    # 판별종료
    if check == True :
        print("정상 : ")
    else :
        print("비정상 : ")
'''

# [출력결과]
# 정상
#   2001년 1월 1일생 남자

# 비정상
#   1) 유효하지 않은 년/월/일
#   2) 유효성 검사에 맞지 않는다.


# 윤년 탐색
'''
year = int(input("연도를 입력하세요 : "))

if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)) :
    print("{}년은 윤년 입니다.".format(year))

else :
    print("{}년은 윤년이 아닙니다.".format(year))
'''    


# 월일 탐색
'''
import date

test_date = input("월일을 입력하세요 : ")

month = date[0:3]
day = date[2:]

if ((1 <= month <= 12) and (1 <= day <= 31)) :
    print("정상")

else :
    print("비정상")
'''


'''
jumin_num1, jumin_num2 = input("주민번호를 입력하세요 : ").split("-")

# 생년월일 탐색
year = jumin_num1[0:2]
month = jumin_num1[2:4]
day = jumin_num1[4:6]


# 성별 탐색
man = ["1", "3", "9"]
woman = ["2", "4", "0"]



if jumin_num2[0] in man :
    print("{}월 {}일생 남자".format(month, day))

elif jumin_num2[0] in woman :
    print("{}월 {}일생 여자".format(month, day))

else :
    print("{}월 {}일생 외국인".format(month, day))
'''

# 유효성 검증
'''
key = 11
logic = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
middle_num = 0

for index in range(len(logic)) :
    middle_num = middle_num + int(num[index]) * logic[index]

value = key - (middle_num % key)

if str(value) == num[-1] :

else :
    print("유효성 검사에 맞지 않는다.")
'''





