# 11_OOP.py

# 객체지향이란 개념은 '완벽하게' 이해하고 코드를 작성하는건 불가능
#  > 코드를 작성해놓고 차근 차근 개념을 추가하면서 작업

# 객체지향 수업... JAVA 8주(2달)시 3주 이상은 진행
#  > 우리 수업은 개념적인 이해, 이후 밑에 있는 부분 (6번부터)은 '아~~ 그렇구나~~'

'''
    [Object Oriented Programming] - 객체지향 프로그래밍
        - 객체지향이론
            실제 세계는 사물(객체)로 이루어져 있으며,
            발생하는 모든 사건들은 사물(객체)간의 상호작용이다.

            이 개념을 토대로 프로그래밍 언어 접목 --> 객체지향 프로그래밍

        - 특징 (장점)
            1. 코드의 재사용성이 높다. (함수 배울 때, 높은 재사용성)
            2. 코드를 관리하기 좋다. (편하다.)
            3. 프로그램의 신뢰성이 높아진다.

        - '클래스'와 '객체'
            1. 클래스는 일종의 설계도(또는 틀)이며,
               객체는 그 설계도를 통해 만들어진 실제 사물
                   아이폰8 설계도 --> 아이폰8 (S/N : 1)
                                     아이폰8 (S/N : 2)

            2. 클래스 (class)
                - 정의 : 객체(사물)를 정의해 놓은 것 (어떠한 객체를 만들 것인지)
                - 용도 : 객체를 생성

            3. 객체 (object)
                - 정의 : 실제로 존재하는 것. (사물 같은..)
                - 용도 : 클래스에 정의된 대로 사용한다.
            
        - 객체 / 인스턴스
            1. 인스턴스 (instance)   :  사례, 경우, 실체
                - 기본적으로는 객체와 같은 의미
                - 문장에서 쓰임에 따라 구분한다.
                    * 클래스(설계도)를 통해 실제로 만들어진 객체를 '인스턴스'라고 한다.

                    아이폰8은 객체이다.
                    아이폰8 설계도(클래스)로 객체를 만들 수 있다.
                    내가 가지고 있는 아이폰8은 인스턴스이다.

        - 객체의 구성 요소 : 속성, 기능
            (속성 : 아이폰8의 색상 등..  /  기능 : 아이폰8으로 사진을 찍는다)

            1. 객체는 클래스에서 정의한 다수의 속성과 기능을 가질 수 있다.
            2. 속성 = 변수
            3. 기능 = 함수

        - 클래스를 비유할 때..
            붕어빵 틀 (클래스) / 만들어진 붕어빵 (객체)
            자동차 공장 (클래스) / 출고된 자동차 (객체)
'''

# 일단 클래스 작성해서 객체를 만들고 다루어보기

class Car :
    # class 바로 안쪽으로 1번 들여쓰기된 구간은
    # 이 클래스에 정의할 '변수' 선언과 '함수' 정의 밖에 할 수 없다.
    #  > print() 등의 명령을 하는 구간이 아니다! 변수, 함수를 만들기만 할 수 있다.
    pass

def func() :
    # 여기는 명령을 내리는 구간 (이 함수가 호출됐을 때 수행할 코드들)
    pass

# 클래스 내부에 정의하는 함수 (객체로만 사용가능한 함수) = 메서드(method)
# 메서드는 반드시 최소 1개의 '매개변수'가 필요하다. (파이썬만~~)
# self ?
#  > 이 메서드를 호출하는 객체 자체가 통째로 대입되는 매개변수
#  > '나'를 의미하는 self (이름이 꼭 self 일 필요는 없다)
#  > bmw.power_on() 을 하면, 그 순간에는 self에 bmw가 대입된다.

class Car :
    # Car로 만들어진 '객체/인스턴스'가 할 수 있는 첫번째 기능(함수)
    def power_on(self) :
        print("부릉부릉~!")
    # end : power_on

    # 두번째 기능
    def drive(self) :
        self.speed = 60 # 주행속도 
        print("주행 시작!")
    # end : drive
# end : Car
'----------------------------------------------------------'
# 함수를 정의(def)하기만 하면, 코드가 수행되지 않듯이
# 클래스도 만들어두기만 하면, 코드의 흐름에 영향이 없다. (자동차 공장만 건설)
'----------------------------------------------------------'
# 인스턴스(객체) 생성 방법 --> 클래스명()
bmw = Car()
# Car는 클래스이기 때문에, 눈에 보이지 않는 '객체'라는게 <생성>
#  1) Car()   코드에 의해 객체가 생성됐고,
#  2) bmw =   코드에 의해 방금 만들어진 객체가 bmw 변수에 '대입'
#  3) 우리는 방금 만든 객체(자동차)를 bmw 변수로 다룰 수 있다.
'----------------------------------------------------------'
Car()
# 이 코드도 또 다른 자동차 1대(객체)를 만드는 코드이지만...
# 변수에 대입되지 않았기 때문에, 우리가 다룰 수 없게 된다. (떠돌이)
#  > 다룰 수 없는 객체는 파이썬이 자동으로 제거한다. (메모리 관리)

# 객체.   --> 내부'맴버' 접근 방법
bmw.power_on()
bmw.drive()
#power_on() # 오류! Car 클래스 내부에 정의된 함수는 Car의 객체로만 사용 가능
'----------------------------------------------------------'
# <객체에 속성(변수) 추가하기>
bmw.model = "BMW" # 대입(=) 코드에 의해, bmw객체에 model속성(변수)가 생성된다.
print( bmw.model )

tico = Car() # 위에 만든 객체랑 아무 상관없는 '새로운 객체 생성'
#print( tico.model ) # 오류!! bmw 객체에만 만들어진 속성(변수) model
tico.engine = "1000cc"
#print( bmw.engine ) # 오류! tico만 engine이 있다!
'----------------------------------------------------------'
# <참고>
# JAVA(객체지향언어)에서는, 객체가 지니는 속성(변수)은 모두 똑같다. (서로 값이 다를순있음)
# 그치만 파이썬은 위처럼, 각각의 객체별로 속성을 다르게 지닐 수 있는 특성이 있다.
'----------------------------------------------------------'
print( bmw.speed )
#print( tico.speed ) # 오류

# self에는 호출하는 객체 자체가 대입된다고 했었음!
#  (1) bmw.drive()  -> bmw 객체가 drive()메서드 호출!
#  (2) drive() 코드 안에서, self.speed = 60    --> bmw.speed=60과 같다.
#       > 왜? self에는 bmw가 대입됐으니까...
#       > 이 시점에 bmw에게 speed 변수가 만들어진 것!
#  (3) 하지만, tico는 drive()를 호출하지 않았기 때문에, speed 속성이 없다..
#      > tico.drive() 를 하면 tico도 speed=60 이 생성이 될 것이다~!


# 1. 클래스를 왜 사용할까??
#  클래스 없이 자동차 2대를 다루어보기 - 모델명, 시동on/off 여부, 최고 주행 가능 속도
'''
car1_model      = "BMW"  # 모델명
car1_power      = False  # 시동 on/off 여부
car1_maxSpeed   = 200    # 최고속도

car2_model      = "SONATA"  # 모델명
car2_power      = True  # 시동 on/off 여부
car2_maxSpeed   = 180    # 최고속도

# 자동차가 '주행'하는 함수(기능)을 만들어보기
def drive_car( model, power, maxSpeed, speed ) : # 모델명, 시동 최고속도,주행할 속도
    print( "[{}] 주행 준비..".format(model) )
    # 시동이 꺼져있으면 주행하지 않는다. (함수종료)
    if power == False :
        print("주행불가 : 시동을 켜주세요.")
        return
    # 주행할 속도가 최고속도보다 빠르면, 경고 출력 후 속도를 낮춘다.
    if speed > maxSpeed :
        print( "주행경고 : 최고속도는 {}km입니다. 속도를 낮춥니다.".format( maxSpeed ) )
        speed = maxSpeed # 최고속도로 주행속도를 변경
    print( "{}km로 주행합니다. 안전운전 하세요.".format(speed) )

drive_car( car1_model, car1_power, car1_maxSpeed, 200 )
drive_car( car2_model, car2_power, car2_maxSpeed, 200 )
'''


#문제점
# (1) 자동차가 늘어나면.. 변수의 수가 엄청 늘어남.. (1대당 3개씩)
# (2) 함수와 변수들간의 '연관성'이 없다. --> 매개변수로 매번 값을 줘야만한다. (불편)

'''
# 만약 이렇게 리스트로 하면, 변수 3개를 변수 하나로 줄일 수는 있지만...
# 함수한테 이 리스트를 '전달'해줘야 한다는 개념은 동일 (함수와 변수의 연관성이 없다.)
car1_list = ["BMW", False, 200]
car2_list = ["SONATA", True, 180]

drive_car(car1_list, 200)
drive_car(car2_list, 200)
'''


# 2. 클래스의 사용 (1)
'''
class Car :
    def drive_car( self, speed ) : 
        print( "[{}] 주행 준비..".format(self.model) )
    
        if self.power == False :
            print("주행불가 : 시동을 켜주세요.")
            return
    
        if speed > self.maxSpeed :
            print( "주행경고 : 최고속도는 {}km입니다. 속도를 낮춥니다.".format( self.maxSpeed ) )
            speed = self.maxSpeed # 최고속도로 주행속도를 변경
        print( "{}km로 주행합니다. 안전운전 하세요.".format(speed) )
# end : Car

car1 = Car() # 객체 1 생성
car2 = Car() # 객체 2 생성

car1.model      = "BMW"  # 모델명
car1.power      = False  # 시동 on/off 여부
car1.maxSpeed   = 200    # 최고속도

car2.model      = "SONATA"  # 모델명
car2.power      = True  # 시동 on/off 여부
car2.maxSpeed   = 180    # 최고속도

# self에는 메서드를 호출하는 '객체' 자체가 자동 대입!
# 만약 메서드에 두개 이상의 매개변수가 존재한다면... self를 제외한 두번째 매개변수부터는 값을 줘야한다.
car1.drive_car(200) # self=car1 , speed=200
car2.drive_car(200) # self=car2 , speed=200
'''

# 클래스와 객체의 개념은 여기까지가 끝!!
# 객체 안에 여러 속성들을 모아놓고 (변수들),
# 이 객체가 만들어진 클래스에 정의된 메서드(함수)를 편하게 사용할 수 있다.

'----------------------------------------------------------------------------'
# 여기서부턴! 객체지향 프로그래밍을 좀 더 효율적이고 편하게 다룰 수 있는 스킬, 방법론들!
print()

# 3. 클래스의 사용 (2) - 생성자란
# 생성자 메서드(함수)
#  (1) 인스턴스(객체) 생성 시 자동으로 호출되는 <메서드/함수>
#  (2) 파이썬 규칙 : 메서드 이름을 반드시 __init__ 으로 해야 '자동 호출'이 된다.
#  (3) 
'''
class Car :
    def __init__(self, n) :
        print("객체가 생성되었다!!")
        self.name = n

Car("BMW") # 객체를 생성하는 코드는, 알고보니!! 생성자를 호출하는 코드였다!! 두둥.

car1 = Car("SONATA")
# (1) Car() 에 의해 객체가 만들어지고, 생성자가 호출된다.
# (2) 생성자의 self에는 지금 만들어지는 객체가 대입 (아직 변수에 대입 전)
# (3) 생성자 코드가 수행이 끝나면, car1 변수에 객체가 대입된다. (속성name이 존재하는 상태)

print("----")
car2 = Car("TICO")
print( car1.name )
print( car2.name )
'''
# 생성자를 사용하는 이유        <--- 엄청 중요한 개념
#  (1) 모든 객체에 공통적인 변수를 만들어 줄 수 있다.
#        > 객체 생성 시 무조건 호출되니까! (self.~~ 하면 된다.)

#  (2) 그 속성을 객체마다 다르게 값을 부여할 수 있다.
#        > 생성자는 메서드니까, 매개변수로 값을 받아서 대입시킬 수 있다!

#  결론 : 객체의 속성(변수) 초기화 (생성/값 대입) 를 편하게 할 수 있다. (생성과 동시에)
'----------------------------------------------------------------------------'

# 4. 클래스의 사용 (3) - Car 클래스에 생성자 만들기
'''
class Car :
    # 생성자에서 초기값으로 반영할 model,power,maxSpeed를 받아서 속성을 추가해보기
    def __init__(self, m, p, maxSpeed) :
        self.model = m
        self.power = p
        self.maxSpeed = maxSpeed
        # 매개변수로 사용된 이름은 아~~무런 상관이 없다.
        # self.maxSpeed <-- 이 객체에 추가할 속성(변수)의 이름
        # = maxSpeed    <-- 매개변수의 이름 (호출 시 전달한 값이 들어있다.)
        
    def drive_car( self, speed ) : 
        print( "[{}] 주행 준비..".format(self.model) )
    
        if self.power == False :
            print("주행불가 : 시동을 켜주세요.")
            return
    
        if speed > self.maxSpeed :
            print( "주행경고 : 최고속도는 {}km입니다. 속도를 낮춥니다.".format( self.maxSpeed ) )
            speed = self.maxSpeed # 최고속도로 주행속도를 변경
        print( "{}km로 주행합니다. 안전운전 하세요.".format(speed) )
# end : Car

car1 = Car("BMW", False, 200) # 객체 1 생성
car2 = Car("SONATA", True, 180) # 객체 2 생성

# self에는 메서드를 호출하는 '객체' 자체가 자동 대입!
# 만약 메서드에 두개 이상의 매개변수가 존재한다면... self를 제외한 두번째 매개변수부터는 값을 줘야한다.
car1.drive_car(200) # self=car1 , speed=200
car2.drive_car(200) # self=car2 , speed=200
'''

# 5. 클래스 내부에서 사용되는 '변수'와 '메서드'의 종류
#    클래스 변수, 인스턴스 변수
#    클래스 메서드, 인스턴스 메서드
#      > 클래스xx, 인스턴스xx
'''
    - 클래스변수
       1. 클래스 내부에 생성    (engine="2000cc")
       2. 클래스메서드에서 생성 (cls.clsValue="~~")
       3. 클래스 외부에서 생성  (Car.wheel=4)

    - 인스턴스변수
       1. 생성자에서 생성 (self.model=m)
           > 모든 인스턴스에 동일하게 생성할 수 있다.
       2. 인스턴스메서드에서 생성 (생성자와 동일)
           > 이 메서드를 호출한 인스턴스에서만 생성
       3. 클래스 외부에서 생성 (car1.color="red")
           > 해당 객체에만 생성
    > 클래스변수, 클래스메서드는 객체를 생성할 필요 없이, 기능을 제공하고 싶을 때 사용
'''
'''
class Car : # 클래스의 코드에는 '변수' 선언과, '매서드' 정의를 할 수 있다.
    engine = "2000cc" # 클래스 변수

    # 아무것도 안 쓰면 기본이 '인스턴스 메서드'
    def instMethod(self) : # instance
        print("나는 인스턴스 메서드!")
        print("객체(인스턴스)를 통해서만 호출할 수 있다. (self에 객체가 들어와야함)")

    @classmethod # 데코레이터(장식자) - 이렇게 써놔야 클래스메서드가 된다.
    def clsMethod(cls) : # class
        print("나는 클래스 메서드!")
        print("매개변수 이름만 바꾼다고해서 클래스메서드가 되지 않음..")
        print("나는 클래스명 또는 객체를 통해 호출할 수 있다. (클래스변수와 비슷")
        cls.clsValue = "난 클래스변수"

    

print( Car.engine )
# 클래스 변수는 이 클래스에 만들어지는 변수 (객체마다 만들어지는 변수가 아님)
# 객체 생성과 상관 없이, '클래스명'으로 사용할 수 있다.

car1 = Car() # 객체1 생성
print( car1.engine ) # 객체를 통해서도 클래스변수를 다룰 수 있다. (좋은 접근방법이 아님)

car1.color = "red" # 인스턴스 변수 (car1이라는 객체에만 존재하는 변수)

car2 = Car()
#print( car2.color ) # 오류! color는 car1 객체에만 존재하는 변수

#print( Car.color ) # 오류! 클래스명으로는 인스턴스 변수를 다룰 수 없다. (누구껄 찾지??)

Car.wheel = 4 # 클래스명으로 만드는 변수 ==> 클래스 변수
print( car2.wheel )

# 메서드
car1.instMethod()
#Car.instMethod() #오류! 클래스명으로 인스턴스메서드 사용 불가 (self에 대입될 객체가 없다)

Car.clsMethod() # cls 매개변수에는 Car 대입
car2.clsMethod() # cls 에는 car2가 Car의 객체니까, Car 대입
print( car1.clsValue ) # clsMethod() 안에서 만들어진 클래스변수!
'''


print()
# 6. 외부 접근 제어
#  외부? 클래스가 정의된 코드 바깥 (클래스를 사용한느 구간)
#  public  : 외부 접근 가능(제어X)
#  private : 외부 접근 불가 -> 클래스 코드 바깥에선 사용할 수 없다. (비공개)

# 변수,메서드 이름 지을 때 그냥 지으면 public
# 이름 앞에 __ (언더바2개) 붙이면 private
#  > 작명에 따라 성질이 변한다.

class Person :
    name = "이몽룡"
    __age = 20

    def publicMethod(self) :
        print("공개된 메서드")
        print( self.__age ) # 클래스 코드 내부에선 제한없이 사용 가능!!
        self.__privateMethod() # 내부니까 사용 가능!
        # self에 p가 대입 --> 다시 그 p 객체로 __privateMethod 호출!

    # 비공개메서드의 목적 : 내부에서만 호출하려고
    def __privateMethod(self) :
        print("비공개 메서드")

    # __age 의 값을 세팅하는 setter
    @classmethod
    def setAge(cls, age) : # set변수명
        # 신뢰성을 향상시키는 예외처리
        if age < 1 :
            age = 1
        elif age > 150 :
            age = 150
        cls.__age = age # 전달받은 값을 private 변수에 대입

    # __age 의 값을 반환하는 getter (가르쳐주는 목적)
    @classmethod
    def getAge(cls) :
        return cls.__age

print( Person.name )
#print( Person.__age ) # 오류! __age는 비공개 (밖에선 접근불가)
#print( Person.age ) # 오류! 이런 이름의 변수는 없다.

p = Person()
p.publicMethod()
#p.__privete # 오류! 비공개
'-------------------------------------------'
# 그럼 왜 이런 성질을 만들었을까?
# ex) 사람 나이가 1살 ~ 150살 까지의 범위인데,
#     age 변수가 public이었다면, 외부에서 아무 값이나 대입 가능 (음수, 0, 1000, 등)
#     이 Person클래스를 만든 사람은 그런 값을 원하지 않는다.
#     외부(클래스를 사용하는 사람)에서 마음대로 다룰 수 없게 비공개 처리!
#      >> 신뢰성 향상

#     대신, 비공개변수를 다룰 수 있는 공개된 메서드를 제공
#      - setter : 비공개변수에 값을 저장할 수 있는 메서드 명칭
#      - getter : 비공개변수의 값을 반환해주는 메서드 명칭

Person.setAge(50)
print( "나이 :", Person.getAge() )


# 7. 상속
'''
    - 물려받는다.
    - 클래스 간의 상속 = 기존 클래스의 멤버들을 사용할 수 있다
    - 부르는 명칭
        부모클래스, 슈퍼클래스
        자식클래스, 서브클래스

    - 오버라이딩 (overriding)
        > 상속 받은 부모클래스의 메서드를 사용 lee.print_info()
          >> Student 클래스에 print_info()가 없어서 부모클래스꺼를 사용
          >> Person에도 print_info()가 없었으면, 코드 오류

        > 부모클래스에 존재하는 메서드를 내 클래스에서 다시 정의하는 것 (재정의)
          >> 나한테도 똑같은 메서드가 존재하니까, 내 껄 사용 (부모꺼 찾지 않고 무시)
'''
print()

class Person :
    def sleep(self) :
        print("사람은 잠을 8시간 잡니다...")

class Student(Person) : # 물려받고 싶은 클래스이름을 () 안에 적는다.
    def study(self) :
        print("학생은 4시간 공부합니다..")

    # 상속 받은 클래스에 존재하는 메서드를, 내가 다시 정의한 것 (재정의 : overriding)
    # 부모의 메서드가 무시되고 내 것이 호출! (나한테서 먼저 메서드를 찾는다.)
    def sleep(self) :
        print("학생은 잠을 6시간 잡니다...")

p = Person()
p.sleep()

s = Student()
s.sleep()
# Student가 sleep()을 사용하려 하는데, 나한테 정의된게 없으니까
# 상속 받은 부모클래스인 Person에서 sleep()을 찾아서 사용! (Person에도 없었으면 오류)

s.study()
#p.study() # 오류! Person에는 이런 메서드 없음. <난 나일뿐...>
# 상속 관계는 자식 -> 부모 아주 일방적인 관계 (부모/자식 용어도 자식입장에서만 적용)

# 상속 관계 (is-a) ~~는 ~~다.
# 학생은 사람이다. (O)
# 사람은 학생이다. (X)


# 8. 추상클래스
'''
    - 추상적인 개념을 가지고 있는 클래스
    - 추상적인 개념 : 추상메서드

    - 추상메서드 : 자식클래스(나를 상속 받는 클래스)가
                  반드시 오버라이딩(재정의)해야하는 메서드

[사용방법]
abc 라는 모듈 필요 (abstract base class)
'''

from abc import *

class Animal(metaclass=ABCMeta) : # 동물
    @abstractmethod
    def cry(self) :
        print("동물은 소리내어 울음운다~~!")
        print("여기서 각 동물이 어떻게 우는지 모른다..")
        print("나를 상속받는 실제 동물 클래스에서 cry를 오버라이딩했으면 좋겠다!")

# 추상클래스 Animal을 상속 받고서, 그 안의 추상메서드 cry()를 오버라이딩 하지 않으면..
# Cat도 추상클래스가 되어 버린다..
# 추상클래스는 '미완성' 클래스 (추상적인 개념 때문에) 라서, 객체를 생성할 수 없다.

#class Cat(Animal) : # 고양이는 동물이다.
#   pass

class Cat(Animal) : # 고양이는 동물이다.
    def cry(self) :
        print("야옹~ 야옹~")

class Mouse(Animal) : # 쥐는 동물이다.
    def cry(self) :
        print("찍!찍!")

print()
tom     = Cat()
jerry   = Mouse()

tom.cry()
jerry.cry()


# <강제성>을 부여하기 위한 목적으로 사용하는 클래스 ==> 추상클래스
