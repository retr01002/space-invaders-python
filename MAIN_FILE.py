import pygame
import time
import random

pygame.init()

red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
green=(0,200,0)
blue=(0,0,255)

display_height=500
display_width=700
gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SPACE INVADER")
clock=pygame.time.Clock()
t1=pygame.time.get_ticks()

spc_img=pygame.image.load(("spaceship_1.jpg"))
al_1_img=pygame.image.load(("alien_.jpg"))
al_2_img=pygame.image.load(("alien2_.jpg"))
#al_3_img=pygame.image.load(("_alien3_.jpg"))
bul_img=pygame.image.load(("bul_1_.jpg"))


factor=1

points=0
highscore=points

lyf_1=0

#bul
bul_state="loaded"

x_al=random.randrange(0,display_width-41)
y_al=-100

x_al_1=random.randrange(0,display_width-41)
y_al_1=-200

'''x_al_2=random.randrange(0,(display_width-(display_width * 0.45)-16-3))
y_al_2=-450'''

aliens=[al_1_img,al_2_img]
no_of_aliens=3

def alien1(a,b):
    gamedisplay.blit(al_1_img,(a,b))

def alien(a,b):
    gamedisplay.blit(al_2_img,(a,b))

'''def alien2(a,b):
    gamedisplay.blit(al_3_img,(a,b))'''
    
def spaceship(x,y):
    gamedisplay.blit(spc_img,(x,y))

def fire(a,b):
    global bul_state
    bul_state="fire"
    gamedisplay.blit(bul_img,(a+(16+2.8),b-22))

def point(a,b):
    global points
    txt1=pygame.font.SysFont("arimo",20)
    textsurface=txt1.render("Score:"+str(points), True, red)
    gamedisplay.blit(textsurface,(a,b))

    pygame.display.update()

def kill():
    global x_al
    global y_al
    global points
    global factor
    
    x_al=random.randrange(0,display_width-41)
    y_al=-100

    points+=1

    factor+=0.045

def kill_1():

    global x_al_1
    global y_al_1
    global points
    global factor
    
    x_al_1=random.randrange(0,display_width-41)
    y_al_1=-200

    points+=1

    factor+=0.045
    
'''def kill_2():

    global lyf_1
    global x_al_2
    global y_al_2
    global points

    x_al_2=random.randrange(0,(display_width-(display_width * 0.45)-16-3))
    y_al_2=-450

    points+=3

    lyf_1=0'''

def show_score():
    global points

    txt1=pygame.font.SysFont("arimo",30)
    textsurface=txt1.render("Your Score : "+str(points), True, red)
    textrect=textsurface.get_rect()
    textrect.center=((display_width/2),(display_height/2)-30)
    gamedisplay.blit(textsurface,textrect)

    pygame.display.update()

    replay_txt()
    qt_txt()    

def show_hs():
    global highscore

    txt1=pygame.font.SysFont("courier",30)
    textsurface=txt1.render("HIGH SCORE : "+str(highscore), True, white)
    textrect=textsurface.get_rect()
    textrect.center=((display_width/2),(display_height/2)+25)
    gamedisplay.blit(textsurface,textrect)

    pygame.display.update()

    time.sleep(1)
    
def qt_txt():
    txt1=pygame.font.SysFont("courier",25)
    textsurface=txt1.render("PRESS ESC TO QUIT GAME", True, red)
    textrect=textsurface.get_rect()
    textrect.center=((display_width/2),(display_height/2)+150)
    gamedisplay.blit(textsurface,textrect)

    pygame.display.update()

    #time.sleep(1)

def replay_txt():
    global highscore
    if highscore<points:
        highscore=points
        
    txt1=pygame.font.SysFont("courier",25)
    textsurface=txt1.render("PRESS RETURN TO PLAY AGAIN", True, red)
    textrect=textsurface.get_rect()
    textrect.center=((display_width/2),(display_height/2)+100)
    gamedisplay.blit(textsurface,textrect)

    pygame.display.update()

    #time.sleep(1)

def msg_disp(text):
    
    gamedisplay.fill(black)
    txt1=pygame.font.SysFont("courier",80)
    textsurface=txt1.render(text, True, red)
    textrect=textsurface.get_rect()
    textrect.center=((display_width/2),(display_height/2)-200)
    gamedisplay.blit(textsurface,textrect)

    pygame.display.update()

    show_score()
    show_hs()

def replay():
    global points
    global highscore

    if highscore<points:
        highscore=points
    points=0
    gameloop()

def qt():
    pygame.quit()
    quit()
    
def dead():
    msg_disp("GAME OVER")
    #print("GAME OVER")

    loop=False

    while not loop:
        for event in pygame.event.get():
            if event.type==12:
                pygame.quit()
                quit()
            if event.type==2:
                if event.key==pygame.K_RETURN:
                    loop=True
                    replay()
                if event.key==pygame.K_ESCAPE:
                    loop=True
                    pygame.quit()
                    quit()

def gameloop():

    global lyf_1
    global points
    global x_al
    global y_al
    global x_al_1
    global y_al_1
    #global x_al_2
    #global y_al_2
    global aliens
    global no_of_aliens
    global t1
    global factor

    #seconds=(pygame.time.get_ticks()-t1)/1000

    factor=1
    
    lyf_1=0

    x_spc=(display_width * 0.45)
    y_spc=(display_height * 0.88)+3

    x_spc_change=0

    x_al=random.randrange(0,display_width-41)
    y_al=-100
    alien_speed=2.5*factor

    x_al_1=random.randrange(0,display_width-41)
    y_al_1=-200
    alien_1_speed=2*factor

    '''x_al_2=random.randrange(0,(display_width-(display_width * 0.45)-16-3))
    y_al_2=-450
    alien_2_speed=0.5   ''' 

    x_bul=x_spc
    y_bul=y_spc
    bul_speed=20*factor

    seconds=(pygame.time.get_ticks()-t1)/1000

    global bul_state
    

    killed=False


    while not killed:

        
        for event in pygame.event.get():
            
            if event.type==pygame.QUIT or event.type==12:
                killed=True
                pygame.quit()
                quit()
                
            if event.type==2:
                if event.key==pygame.K_LEFT:
                    x_spc_change=-5
                    #print("left")
                if event.key==pygame.K_RIGHT:
                    x_spc_change=5
                    #print("right")
                if event.key==pygame.K_SPACE:
                    if bul_state=="loaded":
                        x_bul=x_spc
                        fire(x_bul,y_bul)
                '''if event.key==pygame.K_ESCAPE:
                    qt()
                if event.key==pygame.K_RETURN:
                    replay()'''
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_spc_change=0
            #print(event)
        alien_speed=2.5*factor
        alien_1_speed=2*factor  


        if x_spc>=(700-49):
            x_spc-=5
        elif x_spc<=0:
            x_spc+=5
        else:
            x_spc+=x_spc_change*factor

        y_al+=alien_speed
        y_al_1+=alien_1_speed
        #y_al_2+=alien_2_speed
        

        gamedisplay.fill(black)

        alien(x_al,y_al)
        alien1(x_al_1,y_al_1)
        #alien2(x_al_2,y_al_2)
        spaceship(x_spc,y_spc)
        
        pygame.draw.rect(gamedisplay,red,[0,y_spc-2,display_width,1.5])
            
            
        if y_al+32>=y_spc:
            dead()
            #killed=True
        if y_al_1+32>=y_spc:
            dead()
            #killed=True
        '''if y_al_2+35>=y_spc:
            dead()'''

        if y_bul<y_al+32:
            #print("bul crossed y_al")

            if (x_bul>x_al and x_bul<x_al+41) or (x_bul+20>x_al-10 and x_bul+20<x_al+41):
                kill()
                #print("x")

        if y_bul<y_al_1+32:
            #print("bul crossed y_al")

            if (x_bul>x_al_1 and x_bul<x_al_1+41) or (x_bul+20>x_al_1-10 and x_bul+20<x_al_1+41):
                kill_1()
                #print("x")
            

        '''if y_bul<y_al_2+35:
            #print("bul crossed y_al")

            if x_bul>=x_al_2 and x_bul<=x_al_2+58:
                lyf_1+=1
                print(".")
                if lyf_1==3:
                    kill_2()
                #print#("2 reset")
            if x_bul+16>=x_al_2 and x_bul+16<=x_al_2+58:
                lyf_1+=1
                print(".")
                if lyf_1==3:
                    kill_2()
                #print#("2 reset")'''
                
        if y_bul<=0:
            y_bul=y_spc
            bul_state="loaded"
            
        if bul_state=="fire":
           fire(x_bul,y_bul)
           y_bul-=bul_speed

        point(10,10)
   
        pygame.display.update()
        clock.tick(60)
gameloop()
pygame.quit()
quit()
