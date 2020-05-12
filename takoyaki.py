import pygame,sys,threading,random,time
from timerGame import *
from goalGame import *
from angryGame import *
from multiprocessing import Queue

############### 기본 세팅 초기화 ###############
clock = pygame.time.Clock()
pygame.font.init()

##### image load
icon = pygame.image.load('./images/icon.png')
introBg = pygame.image.load('./images/introBg.png')
modeBg = pygame.image.load('./images/modeBg.png')
storeBg = pygame.image.load('./images/storeBg.png')
startnotice = pygame.image.load('./images/gamenotice.png')
paused = pygame.image.load('./images/paused.png')
end_check = pygame.image.load('./images/end_check.png')
mode1 = pygame.image.load('./images/mode1.png')
mode2 = pygame.image.load('./images/mode2.png')
mode3 = pygame.image.load('./images/mode3.png')
mode1_checked = pygame.image.load('./images/mode1_checked.png')
mode2_checked = pygame.image.load('./images/mode2_checked.png')
mode3_checked = pygame.image.load('./images/mode3_checked.png')
back = pygame.image.load('./images/back.png')

##### sound load
clickS = pygame.mixer.Sound('./sound/click.wav')
keyS = pygame.mixer.Sound('./sound/key.wav')

##### screen setting
screen_width = 1020
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('타코야키 만들기')
pygame.display.set_icon(icon)

##### color set
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
RED = (230, 0, 20)
D_RED = (165, 0, 17)

##### font
smallfont = pygame.font.Font("./NanumPenScript-Regular.ttf",65)
medfont = pygame.font.Font("./NanumPenScript-Regular.ttf",80)

##### 게임 함수 연결
timerGame = TimerMode()   # 제한시간 모드
goalGame = GoalMode()     # 매출액 모드
angryGame = AngryMode()   # 불만도 모드


############### 함수 초기화 ###############

#### text option set
def text_objects(text, color, size = "small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    return textSurface, textSurface.get_rect()

##### text_on_button
def text_on_button(text, color, x, y, w, h, size = "small"):
    textSurf, textRect = text_objects(text, color, size)
    textRect.center = ((x+(w/2)), y+(h/2))
    screen.blit(textSurf, textRect)

##### button_mode
def button_mode(x, y, w, h, action=None):
    cursor = pygame.mouse.get_pos()    #마우스 좌표
    click = pygame.mouse.get_pressed()  #마우스 클릭
    # hover
    if x < cursor[0] < x+w and y < cursor[1] < y+h:
        if 80 < cursor[0] < 80+260 and cursor[1] < 503:
            screen.blit(mode1_checked, (81, 154))
            if click[0] == 1 and action == "mode1":
                clickS.play()
                mode1()
        elif 380 < cursor[0] < 380+260 and cursor[1] < 650:
            screen.blit(mode2_checked, (380, 154))
            if click[0] == 1 and action == "mode2":
                clickS.play()
                mode2()
        elif 680 < cursor[0] < 680+260 and cursor[1] < 940:
            screen.blit(mode3_checked, (676, 154))
            if click[0] == 1 and action == "mode3":
                clickS.play()
                mode3()

##### button_back
def button_back(x, y, w, h, action=None):
    cursor = pygame.mouse.get_pos()    #마우스 좌표
    click = pygame.mouse.get_pressed()  #마우스 클릭
    screen.blit(back, (10, 10))
    # hover
    if 0 < cursor[0] < w and 0 < cursor[1] < h:
        if click[0] == 1 and action == "back":
            print("back")
            clickS.play()
            game_home()

##### mode_choice
def mode_choice():
    start = True
    print("모드 선택")
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                clickS.play()
                quit_check()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:   #q
                    keyS.play()
                    quit_check()
                if event.key == pygame.K_p:
                    keyS.play()
                    game_pause()

        screen.fill((WHITE))    #화면 배경색
        screen.blit(modeBg, (0,0))  #배경화면
        button_mode(80, 153, 260, 350, action="mode1")
        button_mode(380, 153, 260, 350, action="mode2")
        button_mode(680, 153, 260, 350, action="mode3")
        button_back(20, 20, 140, 120, action="back")
        pygame.display.update()
        clock.tick(15)

##### button_in_home
def button_in_home(text, x, y, w, h, color, d_color, action = None):
    # print("button")
    cursor = pygame.mouse.get_pos()    #마우스 좌표
    click = pygame.mouse.get_pressed()  #마우스 클릭
    # hover
    if x+w > cursor[0] > x and y+h > cursor[1] > y:
        # pygame.mixer.Sound.playOnce(hover)
        pygame.draw.rect(screen, color, (x, y, w, h))   #게임시작 버튼
        text_on_button(text, WHITE, x, y, w, h, "medium")
        if 800+210 > cursor[0] > 800 and 570+70 > cursor[1] > 570:
            screen.blit(startnotice, (570, 380))
            if click[0] == 1 and action != None:
                clickS.play()
                mode_choice()
    else:
        pygame.draw.rect(screen, d_color, (x, y, w, h))
        text_on_button(text, GRAY, x, y, w, h)
 
##### game_begin
def game_home():
    begin = True
    while begin:
        # pygame.mixer.music.play(-1) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_check()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    keyS.play()
                    quit_check()
                if event.key == pygame.K_p:
                    keyS.play()
                    game_pause()

        screen.fill((WHITE))    #화면 배경색
        screen.blit(introBg, (0,0))  #배경화면
        button_in_home("PLAY", 800, 570, 210, 70, RED, D_RED, action="modechoice")
        pygame.display.update()
        clock.tick(15)

##### quit_check
def quit_check():
    end = True
    screen.blit(end_check, (0,0))
    pygame.display.update()
    # pygame.mixer.music.pause()  #music
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    keyS.play()
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_n:
                    keyS.play()
                    end = False
                    # pygame.mixer.music.unpause()    #music

##### game pause
def game_pause():
    pause = False
    #text_screen("pause", WHITE, -300, size="large")
    #text_screen("press 'c' to continue", RED, -250, size="medium")
    screen.blit(paused, (0,0))
    pygame.display.update()
    while not pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    keyS.play()
                    pause = True
                elif event.key == pygame.K_q:
                    keyS.play()
                    pygame.quit()
                    quit()

##### game mode
def mode1():
    print('mode1 : 매출액 달성')
    goalGame.main_loop()    #매출액 달성 모드 게임 호출
    game_home()
    
def mode2():
    print('mode2 : 불만도 체크')
    angryGame.main_loop()    #불만도 체크 모드 게임 호출
    game_home()

def mode3():
    print('mode3 : 제한 시간')
    timerGame.main_loop()   #제한시간 모드 게임 호출
    game_home()


############### MAIN ###############
def initGame():    
    pygame.init()
    pygame.mixer.music.load('./sound/bgm.wav')  #music
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1) #music
    game_home()    #게임 초기화면 호출
    
initGame()  #게임 시작