# 10_file_io.py

'''
    [파일 입/출력]  - file input/output
        - PC(disk)에 존재하는 파일의 내용을 읽거나, 쓰거나
            파일을 지우거나 생성하는 등의 행위

        - 디렉토리 (directory)
            > 폴더 또는 디렉토리라고 부른다.
            > 파일과 다른 폴더를 포함할 수 있다.
            > 폴더는 용량이 없다. (항목들을 관리하는 단위)            
            > 폴더는 단지 OS(운영체제)가 어떤 형태로 파일들이 존재하는지
              보여주기만 할 뿐, 실제로 파일을 실행을 하거나 접근을 하면,
              그때 disk에 존재하는 파일의 데이터를 불러온다.
              
        - 파일 (file)
            > 컴퓨터에서 정보를 저장하는 논리적인 단위
            > 파일은 파일명과 확장자로 식별된다. (10_file_io.py)
                >> 전체 파일명에서 맨 뒤에 있는 점(.)만 확장자로 인식
                    test.docx.xlsx.txt  --> txt 파일
                >> 강제로 확장자만 바꾼다고 해서 파일 형식이 바뀌는게 아님
                    (연결프로그램만 변경이 될 뿐...)

            > 모든 파일은 메모장으로 열 수 있다.

            Binary 파일
                메모장으로 열었을 때 내용이 깨진 것처럼 보이는 파일
                특정 프로그램으로 열어야 알아볼 수 있다.
                    (header, tail 등으로 어떤 형식인지 파일에 명시)
                .docx, .xlsx, .hwp 등등...
            
            Text 파일
                메모장으로 열었을 때 알아볼 수 있는 파일
                .txt, .py, .html, .xml 등등...
                    
            기본적으로 프로그래밍 언어에서 파일을 다루게 되면,
            Text 파일 형태로 다룬다. (우리가 할 예정)

            만약, 파이썬으로 엑셀파일을 다루고 싶다거나,
            워드파일을 다루고 싶다면 별도의 모듈을 이용해야 한다.


파일객체 = open("파일명", "파일 열기 모드")

    파일객체 : 변수 (open한 시점부터 이 변수로 파일을 다룰 수 있다.)
    파일명 : 현재 컴퓨터에 존재하는 파일명
            > 절대경로 : (Windows 기준) 드라이브 문자열부터 전체 경로
                C:\test\a\test.txt
            > 상대경로 : 현재 실행하는 위치가 기준이 되는 경로
                ex) 내 소스코드가 C:\test\a\ 폴더에 존재한다면,
                test.txt

    파일 열기 모드
        r : 읽기 모드 (read)   - 읽기만
        w : 쓰기 모드 (write)  - 쓰기만
        a : 추가 모드 (add)    - 파일 마지막에 내용을 추가

        조합된 모드 : r+, w+ 등등..
'''
print("[파일 입출력]")

# 파일 읽기
# 영문, 숫자, 일반 기호들 : 하나당 1byte
# 한글 등의 글자들 :하나당 2byte

# \ 는 문자열에서 '이스케이프 문자'의 기능을 가지게 된다.
# 그래서! 폴더는 구분하는 기호는 \ 가 사용될 땐, \\ 두 개씩 사용해야 하나가 된다.
'''
file = open("C:\\김현수\\python\\소스\\test.txt", "r") # 절대경로

#file = open("test.txt", "r") # 상대경로 (소스파일과 같이 위치)
text = file.read() # 파일의 전체 내용을 '문자열'로 반환한다.
print(text)
file.close() # 사용한 파일은 닫아줘야한다.
'''

# with 를 이용하여 close() 생략하기
'''
with open("test.txt", "r") as file :
    text = file.read()
    print(text)
'''
# with-open 조합에서 close()가 자동으로 수행된다! (들여쓰기 끝날때)

# 파일 내용을 한 줄 씩 읽기(1)
'''
with open("test.txt", "r") as file :
    text_list = file.readlines() # 's' : 한 줄 씩 문자열로 리스트에 추가
    print(text_list) # \n (개행)도 포함이 된다
    print( len(text_list) ) # 이 파일의 줄 개수
    # for문 등을 이용하면 한 줄의 내용씩 다룰 수 있다.
'''

# 파일 내용을 한 줄 씩 읽기(2)
'''
with open("test.txt", "r") as file :
    text = file.readline() # 's'없음 : 한 줄을 문자열로 반환 (\n포함)
    print(text, end='') # print의 개행까지 있으면, 2줄 개행된다.
'''

# readline() 으로 전체 읽기
'''
with open("test.txt", "r") as file :
    while True : # 무한반복
        text = file.readline()

        if not text :
            break
        
        print(text,end='')
'''
# (1) 프로그래밍 언어에선 파일의 내용을 읽거나 쓰고 나면,
#     자동으로 그 다음 읽을 위치/쓸 위치로 이동한다. (위치 = offset)
# (2) 더 이상 읽어진 내용이 없으면, text 변수는 내용이 없다.
#     text 변수에 읽은 내용이 있다 --> True --> not True --> False --> if (X)
#     text 에 내용 없다. --> False --> not False --> True --> if (O) --> break

# 단어, 라인 통계 산출하기
'''
with open("test.txt", "r") as file :
    text = file.read() # 전체 내용 읽기
    word_list = text.split() # 공백, 개행 등의 여백 기준으로 문자열 분리해서 리스트로
    line_list = text.split("\n") # 개행으로만 분리
    #print(word_list)
    #print(line_list)
    print("단어 수 : ", len(word_list))
    print("라인 수 : ", len(line_list))
'''

# 읽은 파일을 for문에 대입하기
'''
with open("test.txt", "r") as file :
    for line in file : # 줄 단위로 대입된다.
        print(line, end='') # 마찬가지로 개행도 같이 포함
'''

# 파일 쓰기 - 항상 파일을 새로 만든다.
with open("test2.txt", "w") as file :
    for i in range(1, 11) : # 1~10이 대입
        text = "{}번째 줄 입니다.\n".format(i)
        file.write(text) # 파일에 문자열 기록
        # 내용을 쓰기만 하니까, 반환 값 필요 없다.
