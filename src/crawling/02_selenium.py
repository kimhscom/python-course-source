# 02_selenium.py

'''
    requests 모듈로는 '페이지 소스 보기'했을 때 내용만 읽을 수 있다.
    브라우저를 통한 접근으로만 읽을 수 있는 내용들이 존재할 수 있다.
    selenium 모듈을 이용하여, 가상의 브라우저를 실행시키고 접근하여, 데이터를 읽는다.
        > 크롬, 오페라, 파이어폭스 등등 다 다룰 수 있다.
        > 크롬으로 실습! --> 같은 폴더에 chromedriver.exe 가 필요
'''

from bs4 import BeautifulSoup # 대소문자 확인
from selenium import webdriver

# (1) 크롬 브라우저 띄우기
driver = webdriver.Chrome() # 객체 생성 (객체 자체가 브라우저)

# (2) 브라우저 페이지 이동 (이동만! 데이터 읽지 않음)
driver.get("https://news.naver.com/")

# (3) 이동된 페이지에서 파싱할 수 있도록 bs4로 변환
soup = BeautifulSoup( driver.page_source.encode("utf-8", "ignore") , "html.parser" )

# 여기서부터 앞에서 requests로 읽어왔던 부분 이후로 동일 코드

# (4) 필요한 데이터 파싱하기
# find( "찾을 태그명", {"그 태그의 속성명":"속성 값"} )
ul = soup.find( "ul", {"class":"section_list_ranking"} )
#print(ul)

data = [] # 빈 리스트 생성 - 나중에 파일로 저장할 내용들을 미리 추가해놓을 리스트

# find_all(find와 사용법 같음) --> 동일한 태그들을 하나씩 리스트의 요소로 만듦
for li in ul.find_all("li") :
    # 10개의 <li> 태그들의 내용이 하나씩 li 변수에 대입된다. (10번 수행)
    rank = li.find("span").text # ~~~.text --> 태그의 일반 텍스트를 문자열로
    title = li.find("a").text.strip()
    print( "{}위 : {}".format(rank, title) )
    data.append( [rank,title] ) # 리스트 뒤에 요소 추가
    # [ ["1", "어쩌구"], ["2", "저쩌구"], ... ]

# 데이터 읽어오기가 끝났으면, 사용한 브라우저를 닫는다.
driver.close() # 브라우저 종료

# (5) 파일로 저장하기
'''
    csv 파일 확장자로 저장
        - comma separated values (쉼표로 구분된 값들)
        - 엑셀이 설치된 경우, 자동으로 '연결 프로그램'이 엑셀로 설정되며
          콤마를 기준으로 분리하여 한 셀 씩 값이 표현된다.
'''

with open("naver_new.csv", "w") as file : # 상대경로 (같은 폴더에 생김)
    file.write("rank,title\n") # 첫번째 줄은 제목 용도로 사용

    for i in data : # 위에서 만든 리스트 요소 하나씩
        file.write( "{},{}\n".format( i[0], i[1].replace(",", " ") ) )
        # 위에서 data.append() 시, 하나의 요소를 '리스트'로 추가했었다.
        # 그때, [rank,title] 로 추가했었기 때문에~~ 뽑아서 쓸 때도 동일한 형태로!
