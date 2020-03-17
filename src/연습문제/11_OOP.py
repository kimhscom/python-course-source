# 클래스 연습하기
'''
    1. 학생 클래스 만들기 (Student)
        속성(변수) : 이름(name), 나이(age), 전화번호(phone), 과목(sub)
        기능(함수)
            1. 생성자 __init__
                > 매개변수로 이름,나이,전화번호,과목을 전달 받고, 각 속성 생성 및 대입
            2. 정보 출력 (print_info)
                > 객체에 만들어져 있는 이름,나이,전화번호 를 출력
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-5678
            3. 공부하기 (study)
                > 객체에 만들어져 있는 이름,과목 출력
                    홍길동 님이 파이썬 공부를 시작합니다.

        - 학생 3명 만들어서 '정보출력', '공부하기' 메서드를 호출해서 출력 결과 확인
            hong.print_info() <-- 이런거 하자는 얘기
'''
'''
class Student :
    def __init__(self, name, age, phone, sub) :
        self.name = name
        self.age = age
        self.phone = phone
        self.sub = sub
        
    def print_info(self) :
        print("이름 : {}".format(self.name))
        print("나이 : {}세".format(self.age))
        print("전화번호 : {}".format(self.phone))
        print("{} 님이 {} 공부를 시작합니다.".format(self.name, self.sub))
        print()

        
hong = Student("홍길동", 20, "010-1234-5678", "파이썬")
lee = Student("이몽룡", 28, "010-9876-5432", "C언어")
sung = Student("성춘향", 25, "010-6789-1234", "JAVA")

hong.print_info()
lee.print_info()
sung.print_info()
'''


'''
    2. 계산기 클래스 (Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 누적
                add_count, min_count, mul_count, div_count

        기능
            1. 생성자 __init__
                > 속성 만들기  (생성자에서 속성을 만든다 = 모든 인스턴스가 공통적으로 속성을 가진다.)
            2. 각 사칙연산을 계산하는 메서드 4개
                > 계산하고 싶은 2개의 값을 전달 받고, 계산 결과를 출력 (반환 X)
                    1 + 2 = 3
            3. 정보 출력(print_info)
                > 각 계산의 수행 횟수 출력

        ex) 덧셈 함수 3번 호출, 나눗셈 함수 2번 호출 후 print_info를 호출하면,
            1 + 2 = 3
            2 + 5 = 7
            10 / 2 = 5.0
            10 / 2 = 5.0
            3 + 9 = 12
            덧셈 : 3
            뺄셈 : 0
            곱셈 : 0
            나눗셈 : 2
'''

class Calc :
    add_count = 0
    min_count = 0
    mul_count = 0
    div_count = 0

    def __init__(self, a, b) :
        self.a = a
        self.b = b
        
    def add(self) :
        print("{} + {} = {}".format(self.a, self.b, (self.a+self.b)))
        Calc.add_count += 1
                
    def min(self) :
        print("{} - {} = {}".format(self.a, self.b, (self.a-self.b)))
        Calc.min_count += 1
     
    def mul(self) :
        print("{} * {} = {}".format(self.a, self.b, (self.a*self.b)))
        Calc.mul_count += 1
    
    def div(self) :
        print("{} / {} = {}".format(self.a, self.b, (self.a/self.b)))
        Calc.div_count += 1

    def print_info(self) :
        print("덧셈 : {}".format(Calc.add_count))
        print("뺄셈 : {}".format(Calc.min_count))
        print("곱셈 : {}".format(Calc.mul_count))
        print("나눗셈 : {}".format(Calc.div_count))

result = Calc(1, 2)
result.add()

result = Calc(2, 5)
result.add()

result = Calc(10, 2)
result.div()

result = Calc(10, 2)
result.div()

result = Calc(3, 9)
result.add()

result.print_info()
