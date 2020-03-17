import pygame as pg
import sys
import random

# (1) pygame 모듈 초기화 (필수)
pg.init()

# (2) 메인 화면 그리기 (screen 객체로 화면을 다룬다)
screen = pg.display.set_mode( (500,650) ) # 화면 크기 500x500
screen.fill( (255,255,255) )              # 배경색 흰색 (rgb)
pg.display.set_caption("가위바위보")        # 화면 제목

# (3) 텍스트 쓰기
fontObj = pg.font.Font('gulim.ttc', 32)    # main 폰트 설정 

# 텍스트1
text_main = fontObj.render ('가위바위보 하자!', True, (0,0,0)) # 내용,부드럽게,글씨색(검정)
text_main_rect = text_main.get_rect()
text_main_rect.center = (250, 50) # 위치
screen.blit(text_main, text_main_rect) # 텍스트 그리기

# 텍스트2
textUC = fontObj.render('USER     vs     COM', True, (0,0,0)) # 내용,부드럽게,글씨색(검정)
textUC_rect = textUC.get_rect()
textUC_rect.center = (250, 300) # 위치
screen.blit(textUC, textUC_rect) # 텍스트 그리기

# 텍스트3
text_score = fontObj.render('점수', True, (0,0,0)) # 내용,부드럽게,글씨색(검정)
text_score_rect = text_score.get_rect()
text_score_rect.center = (250, 520) # 위치
screen.blit(text_score, text_score_rect) # 텍스트 그리기

# (4) 이미지
rock     = pg.image.load('바위.png') # 이미지 3개를 불러와서
scissors = pg.image.load('가위.png')
paper    = pg.image.load('보.png')
r = pg.transform.scale(rock.convert(), (150,150)) # 크기 변환
s = pg.transform.scale(scissors.convert(), (150,150))
p = pg.transform.scale(paper.convert(), (150,150))

# 변환한 이미지 객체 3개를 리스트에 저장
main_rsp = [r,s,p]          # 사용자가 클릭할 이미지 (고정)

# 게임용으로 그려줄 가위바위보 com,user 리스트로 복제
user_rsp = main_rsp.copy()
com_rsp  = main_rsp.copy()

# 클릭할 메인 가위바위보 이미지 그리기 (고정)
screen.blit( main_rsp[0], (10, 100) )
screen.blit( main_rsp[1], (180, 100) )
screen.blit( main_rsp[2], (330, 100) )


# (5) 메인 화면이 켜진 뒤 메인 화면에 대한 이벤트처리를 위한 무한반복
while True :

    # 어떠한 이벤트가 발생했을 때, get()으로 얻어오고, event에 해당 이벤트가 대입
    for event in pg.event.get() :

        if event.type == pg.QUIT : # 종료 눌렀을 때
            pg.quit()
            sys.exit()
            
        elif event.type == pg.MOUSEBUTTONDOWN : # 마우스 버튼이 눌렸을 때

            x, y = event.pos # 버튼이 눌린 위치를 x,y 좌표로 얻어옴

            # '바위' 이미지가 클릭된 것을 감지
            if main_rsp[0].get_rect().move(10,100).collidepoint(x,y) :
                print("바위")
                screen.blit( user_rsp[0], (50, 330) )
                com = random.choice(com_rsp)
                screen.blit( com, (300, 330) )
            # '가위' 이미지가 클릭된 것을 감지    
            elif main_rsp[1].get_rect().move(180,100).collidepoint(x,y) :
                print("가위")
                screen.blit( user_rsp[1], (50, 330) )
                com = random.choice(com_rsp)
                screen.blit( com, (300, 330) )
            # '보' 이미지가 클릭된 것을 감지
            elif main_rsp[2].get_rect().move(330,100).collidepoint(x,y) :
                print("보")
                screen.blit( user_rsp[2], (50, 330) )
                com = random.choice(com_rsp)
                screen.blit( com, (300, 330) )

    # 변경된 화면 새로 그리기
    pg.display.update()


# To do.
#   1. 승무패 판별
#      승 : 점수 +10
#      패 : 점수 -5
#      무 : 변동 X

#   2. 반복 횟수 지정 10회

#   3. 최종 점수 70점 이상 -> "대단하시네요!"
#                0점 미만 -> "분발하세요!" 
