# koreais\my_module.py

my_str = "my_module의 문자열!"

def my_add(a,b) :
    return (a+b)

def my_mul(a,b) :
    return (a*b)

class My_Dog :
    def __init__(self, name="똥개") : # 생성자 메서드=함수=매개변수 초기값 사용가능
        self.name = name

    def cry(self) :
        # 생성자에서 self.name을 만들었으니까, 무조건 존재하는 속성으로 간주하고 사용
        print( "{} : 멍!멍!".format( self.name ) )


# import를 하면, 이 소스파일이 한 줄씩 전체 수행이 되는 원리!
print("이 소스코드가 수행이 되는구나!!")

# 이 소스코드가 수행되는게 '누구'에게 의해서인지 구분할 수 있는 변수가 제공된다.
# 파이썬 기본 제공 '문자열' 변수 : __name__    <-- 규칙
print( "__name : " + __name__ )
# - 내가 실행 주체 : __main__
# - 남이 import 시 : import한 모듈이름

if __name__ == "__main__" :
    print("내가 주체가 되어 실행됐구나!")
    print("이런 if문 안에는 이 모듈의 기능을 테스트할 코드 등을 작성")
    print("내가 지금 제공할 모듈의 기능이 정상인가? 버그는 없나? 확인용도")



