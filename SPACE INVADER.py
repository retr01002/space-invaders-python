import pygame
import time
import random

red=(255,0,0)
black=(0,0,0)
white=(255,255,255)

pygame.init()

dis=pygame.display.set_mode((700,500))
pygame.time.Clock()
def game1():
    txt1=pygame.font.SysFont("courier",30)
    #txt2=pygame.font.Font(txt1,30)
    textsurface=txt1.render("PRESS RETURN TO PLAY GAME", True, red)
    textrect=textsurface.get_rect()
    textrect.center=((700/2),(500/2)+100)
    dis.blit(textsurface,textrect)

    pygame.display.update()

def qt():
    txt1=pygame.font.SysFont("courier",30)
    #txt2=pygame.font.Font(txt1,30)
    textsurface=txt1.render("PRESS ESC TO QUIT GAME", True, red)
    textrect=textsurface.get_rect()
    textrect.center=((700/2),(500/2)+150)
    dis.blit(textsurface,textrect)

    pygame.display.update()

def rules():
    txt1=pygame.font.SysFont("courier",20)
    #txt2=pygame.font.Font(txt1,30)
    textsurface=txt1.render("RULES : Use arrow keys to navigate and spacebar to shoot", True, white)
    textrect=textsurface.get_rect()
    textrect.center=((700/2),(500/2))
    dis.blit(textsurface,textrect)

    pygame.display.update()

def gmply():
    txt1=pygame.font.SysFont("courier",19)
    #txt2=pygame.font.Font(txt1,30)
    textsurface=txt1.render("GAMEPLAY : Prevent the enemies from entering your territory", True, white)
    textrect=textsurface.get_rect()
    textrect.center=((700/2),(500/2)+20)
    dis.blit(textsurface,textrect)

    pygame.display.update()
    
def title():
    dis.fill(black)
    txt1=pygame.font.SysFont("courier",30)
    #txt2=pygame.font.Font(txt1,30)
    textsurface=txt1.render("SPACE INVADER", True, red)
    textrect=textsurface.get_rect()
    textrect.center=((700/2),(500/2)-200)
    dis.blit(textsurface,textrect)

    pygame.display.update()
    
    game1()
    qt()
    rules()
    gmply()

title()

loop=False

while not loop:
    for event in pygame.event.get():
        if event.type==12:
            pygame.quit()
            quit()
        if event.type==2:
            if event.key==pygame.K_RETURN:
                import MAIN_FILE.py
                loop=True
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
                quit()
                
                
             
