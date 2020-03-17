# 딕셔너리 연습
'''
    my_dict에서 한국 뽑아내기
      > hint : 뽑아낸다
'''
my_dict = {"한국":"KOREA", "일본":"JAPAN", "중국":"CHINA"}
##############################
# 여기 1줄만 고쳐서 완성하기  - 나머지 코드는 고치지마세요!!
korea = my_dict.pop("한국")
##############################

print(my_dict)  # 일본,중국의 key,value들만 출력
                # 출력결과 --->  {'일본':'JAPAN', '중국':'CHINA'}
                
print(korea) # 출력결과 --->  KOREA
