# koreais\my_main.py

# my_module을 불러와서 사용하기
#  - import 할 때, 모듈명이 잘못되면 바로 오류!

# (1) 모듈명 그래로 붙여서 사용
'''
import my_module
print( my_module.my_str )
print( my_module.my_add(10,20) )
'''


# (2) 별칭 주기
'''
import my_module as m
print( m.my_str )
'''


# (3) 모듈에서 일부만 불러오기 - 모듈명 생략
'''
from my_module import my_str, my_add # ()없이 이름만 나열!
print(my_str)
#print( my_mul(10,20) ) #오류! 불러오지 않음
'''


# (4) 모듈에서 전체 불러오기

from my_module import *
print(my_str)

# My_Dog 클래스를 이용하여, '바둑이'가 멍멍 짖도록 코드 작성
dog = My_Dog() # name 매개변수에 값을 주지 않아서 초기값 "똥개"가 self.name에..
dog.cry()

baduk = My_Dog("바둑이")
baduk.cry()
