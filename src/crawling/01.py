# 01.py

import requests
from bs4 import BeautifulSoup # 대소문자 확인
from selenium import webdriver

# (1) 웹페이지 데이터 읽어오기 (requests 모듈 이용)

h = { "User-agent" : "Mozilla/5.0" }
url = "https://news.naver.com/"

response = requests.get(url, headers=h) # 해당 url로 정보 요청

# (2) 읽어온 데이터를 파싱하기 좋도록 bs4 객체로 변환
soup = BeautifulSoup( response.content, "html.parser" )
#print( soup ) # html 읽어왔는지 확인

# (3) 필요한 데이터 파싱하기
# find( "찾을 태그명", {"그 태그의 속성명":"속성 값"} )
ul = soup.find( "ul", {"class":"section_list_ranking"} )
#print(ul)

# find_all(find와 사용법 같음) --> 동일한 태그들을 하나씩 리스트의 요소로 만듦
for li in ul.find_all("li") :
    # 10개의 <li> 태그들의 내용이 하나씩 li 변수에 대입된다. (10번 수행)
    rank = li.find("span").text # ~~~.text --> 태그의 일반 텍스트를 문자열로
    title = li.find("a").text.strip()
    print( "{}위 : {}".format(rank, title) )
