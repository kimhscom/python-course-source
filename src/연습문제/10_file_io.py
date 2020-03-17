# 파일 입출력 연습
'''
    test_practice.txt 를 미리 만들어둔다.
[파일 내용]
사랑하는 엄마에게...

안녕하세요. 사랑하는 자식 길동이에요.

그럼이만.


    아래 출력 결과를 구하기
    [출력결과]
    전체 글자 수 : ??
    전체 단어 수 : ??
    전체 라인 수 : ??
    '사랑' 단어 수 : 2
'''
with open("test_practice.txt", "r") as file :
    text = file.read()
    letter_list = list(text)
    word_list = text.split()
    line_list = text.split("\n")
    love_list = text.count("사랑")

    print("[출력결과]")
    print("전체 글자 수 : ", len(letter_list))
    print("전체 단어 수 : ", len(word_list))
    print("전체 라인 수 : ", len(line_list))
    print("'사랑' 단어 수 : ", love_list)
    
