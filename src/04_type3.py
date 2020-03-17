# 04_type3.py

'''
    5. 딕셔너리(Dictionary)
      사전!!
      형태 : {key1:value1, key2:value2, ...}
        > key와 value는 한 쌍
          key = 단어, value = 뜻

      - 문자열 포매팅 함수(format)에서 {키워드} 사용했었음
         "{name}".format(name="한수창")
         이와 비슷한 느낌!

      - 요소가 여러 개 나열된 자료형이긴 한데...
        문자열,리스트,튜플은 '순서'가 있어서 인덱스로 인덱싱
        딕셔너리는 '순서'가 없고, 'key'를 가지고 인덱싱한다.

      - 주의사항
        1. key 값은 중복되면 안 된다.
        2. key 값으로는 리스트,딕셔너리를 사용할 수 없다.
          > key : 변하지 않는 성질의 자료(값) - 숫자,문자,튜플
          > value : 아무거나 상관 없음
'''
print("[딕셔너리 만들기]")
my_dict = {"축구":"Soccer", 2002:"한일", (1,2):("원","투"), "16강":[2002,2010]}
'''
        key       value
        ------------------
        "축구"    "Soccer"       문자열:문자열
        2002      "한일"         정수:문자열
        (1,2)     ("원","투")    튜플:튜플
        "16강"    [2002,2010]    문자열:리스트
'''
print( my_dict )
print( my_dict["축구"] ) # key를 통해서 value 값을 얻어낸다.
# 문자열,리스트,튜플에서 인덱싱할 때 사용했던 index 값들은, 딕셔너리에서는 key와 같다.
#                       하나 하나의 요소들은, 딕셔너리에서는 value와 같다.
a = ["Soccer"]
print( a[0] ) # 인덱스(key)를 가지고 "Soccer" (value)를 얻어낸다.

print( my_dict["16강"][1] ) # 2010 출력!
# key가 "16강"인 요소의 value가 '리스트' [2002,2010] 이다. 여기서 두번째 요소 인덱싱!

print("딕셔너리 요소 추가/삭제")
my_dict[2018] = "F조-3위"
print(my_dict)

del( my_dict[(1,2)] ) # key가 튜플 - 하나의 요소가 통째로 제거!
print(my_dict)

print()

# 관리자에 관련된 항목들을 key:value 형태로
admin_dict = { "id":"admin", "pw":"1234", "name":"관리자" }
print("관리자 id : " + admin_dict["id"])
print("관리자 pw : " + admin_dict["pw"])
print("관리자 name : " + admin_dict["name"])
print()

'''
    6. 집합(Set)
      - 수학에서의 집합을 의미
          > 교집합, 합집합, 차집합 등을 구할 수 있다.

      - 중복된 값을 허용하지 않는다.
          > 중복 제거 용도 사용
      - 순서가 없다. (인덱싱 불가능)
'''
my_set = {1,2,3,1,1,1,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,1,1,2}
print( my_set )

my_set2 = {1,1,2,2,"안녕","안녕","ㅋㅋ","ㅋㅋ"}
print( my_set2 )

my_str = "Hello"
my_set = set(my_str) # 문자열 -> 집합(set) 변환
print(my_set)

my_int = 112233 # int는 정수 (integer)
#my_set = set(my_int) # 오류! 숫자(정수+실수 등)는 유일한 하나의 값
#print( my_int[0] ) # 오류!   > 인덱싱 같은 행위 하지 못함

# 자료형끼리의 변환은 서로 비슷한 성질의 자료끼리 가능

my_list = [1,2,3,1,1,1,1,1,2,1,1,1,3,1,1,2,3,1,2,1,1,1,1,2]
print( my_list )
# 리스트의 중복된 값을 쉽게 제거하고 싶다면!
my_set = set(my_list)  # list -> set
my_list = list(my_set) # set -> list
print( my_list )

'''
    int()   --> 정수로 변환
    float() --> 실수로 변환
        > bin(), oct(), hex() -> 2,8,16진수 변환
    str() ---> 문자열
    list()
    tuple()
    dict()
    set()
    bool()
'''

'''
    7. bool
      - (참고) Java에선 boolean 자료형, C언어에는 없다.

      - 참(True)과 거짓(False)을 표현하는 자료형

      - 자료형의 값에 따른 참과 거짓
          값       True/False
          -------------------
          1        True
          0        False
          "11"     True
          ""       False
          [1,2]    True
          []       False
          ()       False
          None     False     (함수 진도 나갈 때 자주 볼 예정)
          -------------------

          거짓인 경우는
              1. 요소가 없다. (문자열, 리스트 등)
              2. 숫자가 0이다. (0만 아니면 참)
              3. None : 값이 없다는걸 의미하는 '자료형/값'
'''

print()

print( bool(1) ) # 이때 출력되는 True는 문자열이 아니라 bool 자료형의 '값'
print( bool(0) ) # False(거짓)도 마찬가지




