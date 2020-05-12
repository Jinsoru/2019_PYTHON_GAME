import pygame,sys,threading,random,time

pygame.font.init()
pygame.init()

##### global variable
cusCount = 0
cusChange = 0
end = True

##### takoyaki count
final=0

#### tako_board
taco_board={1:{"x":30,"y":365,"status":None},2:{"x":100,"y":365,"status":None},3:{"x":170,"y":365,"status":None},4:{"x":240,"y":365,"status":None},5:{"x":310,"y":365,"status":None},
            6:{"x":30,"y":420,"status":None},7:{"x":100,"y":420,"status":None},8:{"x":170,"y":420,"status":None},9:{"x":240,"y":420,"status":None},10:{"x":310,"y":420,"status":None},
            11:{"x":30,"y":475,"status":None},12:{"x":100,"y":475,"status":None},13:{"x":170,"y":475,"status":None},14:{"x":240,"y":475,"status":None},15:{"x":310,"y":475,"status":None},
            16:{"x":30,"y":530,"status":None},17:{"x":100,"y":530,"status":None},18:{"x":170,"y":530,"status":None},19:{"x":240,"y":530,"status":None},20:{"x":310,"y":530,"status":None},
            21:{"x":30,"y":585,"status":None},22:{"x":100,"y":585,"status":None},23:{"x":170,"y":585,"status":None},24:{"x":240,"y":585,"status":None},25:{"x":310,"y":585,"status":None}}

# 완성된 타코야끼
final_setting={1:{'x':540,'y':365,'status':True},2:{'x':560,'y':365,'status':True},3:{'x':580,'y':365,'status':True},4:{'x':600,'y':365,'status':True},5:{'x':620,'y':365,'status':True}}

##### customer
customers=['./images/person1.png','./images/person2.png','./images/person3.png','./images/person4.png','./images/person5.png','./images/person6.png']
count=[1,2,3,4,5]
ground={1:{'x':130,'y':30,'status':True},2:{'x':440,'y':30,'status':True},3:{'x':740,'y':30,'status':True}}

# 손님 1
a=""
text1=""
cnt_1 = 0
# 손님 2
b=""
text2=""
cnt_2 = 0
# 손님 3
c=""
text3=""
cnt_3 = 0

##### screen setting
display_width = 1020
display_height = 650
white = (255, 255, 255)
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

##### drag status check
c_drag=0
b_drag = 0    #switch with which I am seting if I can move the image
o_drag=0

##### cooker pos
b_x = 540
b_y = 480
o_x = 680
o_y = 480
c_x = 830
c_y = 480

##### image load
cooker=pygame.image.load('./images/cooker.png')
empty=pygame.image.load('./images/mold.png')
first=pygame.image.load('./images/takoyaki1.png')
second=pygame.image.load('./images/takoyaki2.png')
takoyaki3=pygame.image.load('./images/takoyaki3.png')
takoyaki4=pygame.image.load('./images/takoyaki4.png')
tako=pygame.image.load('./images/tako.png')
img = pygame.image.load('./images/kettle.png')   #my image and then his width and height
playscreen=pygame.image.load('./images/timerScreen.png')
timeOverBg =  pygame.image.load('./images/timeOverBg.png')
back = pygame.image.load('./images/back.png')
imgWidth = 100
imgHeight = 100

##### sound load
clickS = pygame.mixer.Sound('./sound/click.wav')
keyS = pygame.mixer.Sound('./sound/key.wav')
noS = pygame.mixer.Sound('./sound/no.wav')
okS = pygame.mixer.Sound('./sound/ok.wav')
sucS = pygame.mixer.Sound('./sound/successEnd.wav')

##### mouse pos
mouse = pygame.mouse.get_pos()
x=mouse[0]
y=mouse[1]
change_x = int(x / 70) * 70 + 30
change_y = int(y / 55) * 55 - 20

##### font
font = pygame.font.Font("./NanumPenScript-Regular.ttf", 50)
font2 = pygame.font.Font("./NanumPenScript-Regular.ttf",100)

##### timer
seconds = 60
time = '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
ok = True

############### 함수 초기화 ###############

class TimerMode():
    def image(self, img,imgX,imgY):   #function to blit image easier
        gameDisplay.blit(img, (imgX, imgY))

    # 익는 거 구현
    def ripe(self, change_x, change_y):
        for a in taco_board.values():
            if a['x'] == change_x and a['y'] == change_y and a['status'] == 2:
                a['status'] = 3

    # 뒤집개 드래그 앤 드롭
    def movableCook(self):   #function in which i am moving image
        global c_drag, c_x, c_y
        c_mouse = pygame.mouse.get_pos()
        c_click = pygame.mouse.get_pressed()

        self.image(cooker,c_x,c_y)

        if c_click[0] == 1 and c_x + imgWidth > c_mouse[0] > c_x and c_y + imgHeight > c_mouse[1] > c_y:  #asking if i am within the boundaries of the image
            if o_drag != 1:
                if b_drag != 1:
                    c_drag = 1                                                                          
        if c_click[0] == 0:   #asking if the left button is pressed
            c_drag = 0
        if c_drag == 1:   #moving the image
            c_x = c_mouse[0] - (imgWidth / 5)
            c_y = c_mouse[1] - (imgHeight / 5)

    # 반죽 드래그 앤 드롭
    def movableban(self):
        global b_drag, b_x, b_y
        b_mouse = pygame.mouse.get_pos()
        b_click = pygame.mouse.get_pressed()

        self.image(img,b_x,b_y)

        if b_click[0] == 1 and b_x + imgWidth > b_mouse[0] > b_x and b_y + imgHeight > b_mouse[1] > b_y:
            if o_drag != 1:
                if c_drag !=1:
                    b_drag=1
        if b_click[0] == 0:
            b_drag = 0
        if b_drag == 1:
            b_x = b_mouse[0] - (imgWidth / 4)
            b_y = b_mouse[1] - (imgHeight / 2)

    # 문어 드래그 앤 드롭
    def moveableTako(self):
        global o_drag, o_x, o_y
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        self.image(tako,o_x,o_y)

        if click[0] == 1 and o_x + imgWidth > mouse[0] > o_x and o_y + imgHeight > mouse[1] > o_y:  #asking if i am within the boundaries of the image
            if b_drag != 1:
                if c_drag != 1:
                    o_drag =1
        if click[0] == 0:   #asking if the left button is pressed
            o_drag = 0

        if o_drag == 1:   #moving the image
            o_x = mouse[0] - (imgWidth / 2)   #imgWidth / 2 because i want my mouse centered on the image
            o_y = mouse[1] - (imgHeight / 2)

    # 손님 랜덤 돌리기
    def rand(self):
        global a,b,c,text1,text2,text3, seconds, cnt_1, cnt_2, cnt_3,cusChange
        
        if cusChange == 1:  # 손님1
            cus1 = random.choice(customers)
            cnt1 = str(random.choice(count))+""
            cnt_1=int(cnt1)
            text1 = font.render(cnt1+"개", True, (28, 0, 0))  #텍스트가 표시된 Surface 를 만듬
            a = pygame.image.load(cus1)
        elif cusChange == 2:
            cus2 = random.choice(customers)
            cnt2 = str(random.choice(count))+""
            cnt_2=int(cnt2)
            text2 = font.render(cnt2+"개", True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
            b = pygame.image.load(cus2)
        elif cusChange == 3:
            cus3 = random.choice(customers)
            cnt3 = str(random.choice(count))+""
            cnt_3=int(cnt3)
            text3 = font.render(cnt3+"개", True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
            c = pygame.image.load(cus3)
        else:
            cus1 = random.choice(customers)
            cus2 = random.choice(customers)
            cus3 = random.choice(customers)
            cnt1 = str(random.choice(count))+""
            cnt2 = str(random.choice(count))+""
            cnt3 = str(random.choice(count))+""
            cnt_1=int(cnt1)
            cnt_2=int(cnt2)
            cnt_3=int(cnt3)
            text1 = font.render(cnt1+"개", True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
            text2 = font.render(cnt2+"개", True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
            text3 = font.render(cnt3+"개", True, (28, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
            a = pygame.image.load(cus1)
            b = pygame.image.load(cus2)
            c = pygame.image.load(cus3)

    # 손님 그리기
    def customer_loop(self):
        global a,b,c,text1,text2,text3
        gameDisplay.blit(a, [ground[1]['x'], ground[1]['y']])
        gameDisplay.blit(b, [ground[2]['x'], ground[2]['y']])
        gameDisplay.blit(c, [ground[3]['x'], ground[3]['y']])
        gameDisplay.blit(text1,[ground[1]['x']+75, ground[3]['y']+5])
        gameDisplay.blit(text2,[ground[2]['x']+75, ground[3]['y']+5])
        gameDisplay.blit(text3,[ground[3]['x']+75, ground[3]['y']+5])

    ##### button_back
    def button_back(self, x, y, w, h, action=None):
        global end, final, b_x, b_y, o_x, o_y, c_x, c_y, cusCount, seconds, time
        cursor = pygame.mouse.get_pos()    #마우스 좌표
        click = pygame.mouse.get_pressed()  #마우스 클릭
        playscreen.blit(back, (10, 10))
        if 0 < cursor[0] < w and 0 < cursor[1] < h:
            if click[0] == 1 and action == "back":
                clickS.play()
                print("back")
                for a in taco_board.values():
                    a['status'] = None
                b_x, b_y, o_x, o_y, c_x, c_y, final, seconds, cusCount = 540, 480, 680, 480, 830, 480, 0, 60, 0
                time = '60'.rjust(3)
                while end:
                    end = False

    # 게임 끝
    def endGame(self):
        global final, b_x, b_y, o_x, o_y, c_x, c_y, cusCount, time
        sucS.play()     #게임끝 효과음
        gameDisplay.blit(font.render('0', True, (0, 0, 0)), (980, 15))
        gameDisplay.blit(timeOverBg, (0,0))
        text = str(cusCount)+"명"
        gameDisplay.blit(font2.render(text, True, (0, 0, 0)), (480, 350))
        pygame.display.update()
        end = True
        for a in taco_board.values():
            a['status'] = None
        b_x, b_y, o_x, o_y, c_x, c_y, final = 540, 480, 680, 480, 830, 480, 0
        cusCount = 0
        while end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        end = False
    
    #### 메인
    def main_loop(self):
        global final,b_x,b_y,o_x,o_y,c_x,c_y,cnt_1,cnt_2,cnt_3,cusChange, end
        self.rand()
        end = True

        while end:
            draw_y = 0
            draw_x = 0
            gameDisplay.fill([255,255,255])
            gameDisplay.blit(playscreen,[0,0])

            # 완성된 타코야끼 화면 출력
            for i in range(1,final+1):
                if final_setting[i]['status']==True:
                    gameDisplay.blit(takoyaki4,[final_setting[i]['x'],final_setting[i]['y']])

            # 불판 화면 출력
            for i in range(1,26):
                if taco_board[i]['status']==None:
                    gameDisplay.blit(empty,[taco_board[i]["x"],taco_board[i]["y"]])
                elif taco_board[i]['status']==1:
                    gameDisplay.blit(first,[taco_board[i]["x"],taco_board[i]["y"]])
                elif taco_board[i]['status']==2:
                    gameDisplay.blit(second,[taco_board[i]["x"],taco_board[i]["y"]])
                elif taco_board[i]['status']==3:
                    gameDisplay.blit(takoyaki3,[taco_board[i]["x"],taco_board[i]["y"]])
                elif taco_board[i]['status']==4:
                    gameDisplay.blit(takoyaki4,[taco_board[i]["x"],taco_board[i]["y"]])
            
            self.customer_loop()

            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                x=mouse[0]
                y=mouse[1]
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # elif event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_q:
                #         pygame.quit()
                #         quit()
                elif event.type == pygame.USEREVENT:
                    global seconds, time, cusCount
                    seconds -= 1
                    if seconds > 0 :
                        time = str(seconds).rjust(3)
                    else:
                        end = False
                        self.endGame()
                        seconds = 60
                        time = '60'
                        cusCount = 0
                elif event.type==pygame.MOUSEBUTTONUP:
                    ###### 타코야키 굽기
                    if 30<x<360 and 635>y>365:
                        change_x = int(x / 70) * 70 + 30
                        change_y = int(y / 55) * 55 - 20
                        if b_drag==1:
                            for a in taco_board.values():
                                if a['x'] == change_x and a['y'] == change_y and a['status'] == None:
                                    a['status'] = 1
                        elif o_drag==1:
                            for a in taco_board.values():
                                if a['x'] == change_x and a['y'] == change_y and a['status'] == 1:
                                    a['status'] = 2
                                    ripeThread = threading.Timer(4.0, self.ripe, args=(change_x, change_y),kwargs=None).start()
                        elif c_drag==1:
                            for a in taco_board.values():
                                if a['x'] == change_x and a['y'] == change_y and a['status'] == 3:
                                    a['status'] = 4
                        elif b_drag!=1 and o_drag!=1 and c_drag!=1:
                            for a in taco_board.values():
                                if a['x'] == change_x and a['y'] == change_y and a['status'] == 4 :
                                    a['status']=None
                                    if final<6:
                                        final+=1
                                elif a['x'] == change_x and a['y'] == change_y and a['status'] == 5 :
                                    a['status']=None
                    ###### 타코야키 판매
                    elif 150 < x < 250 and 240 < y < 315 and final!=0:
                        if final==cnt_1:
                            okS.play()
                            final=0
                            cusCount += 1
                        elif final!=cnt_1:
                            noS.play()
                        cusChange = 1
                        self.rand()
                    elif 460 < x < 570 and 260 < y < 320 and final!=0:
                        if final==cnt_2:
                            okS.play()
                            final=0
                            cusCount += 1
                        elif final!=cnt_2:
                            noS.play()
                        cusChange = 2
                        self.rand()
                    elif 760 < x < 870 and 260 < y < 320 and final!=0:
                        if final==cnt_3:
                            okS.play()
                            final=0
                            cusCount += 1
                        elif final!=cnt_3:
                            noS.play()
                        cusChange = 3
                        self.rand()

            self.movableCook()
            self.movableban()
            self.moveableTako()
            gameDisplay.blit(font.render(time, True, (0, 0, 0)), (950, 15))
            self.button_back(20, 20, 100, 80, action="back")
            pygame.display.update()
            clock.tick(30)