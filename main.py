import pygame
from pygame import mixer
import math
import random

pygame.init()
screen = pygame.display.set_mode((470,600))
pygame.display.set_caption("Sky Shooter")
running = True

#making background
bg = pygame.image.load('bg.jpg')
def background():
    screen.blit(bg, (0,0))
def music():
    music = mixer.music.load('muzic.mp3')
    mixer.music.play(-1)

#making main
main = pygame.image.load('aircraft.png')
main_x = 230
main_y = 500
main_change = 0

def main_dest(x,y):
    screen.blit(main, (x,y))

#making enemy
Enemy = [pygame.image.load('1.png'),
         pygame.image.load('2.png'),
         pygame.image.load('3.png'),
         pygame.image.load('4.png'),
         pygame.image.load('5.png')]
E_x = []
E_y = [30,30,30,30,30]
E_change = [1,0.9,0.8,1.2,0.77]
num_E = 5

for i in range(num_E):
    E_x.append(random.randint(10,370))

def Eneme(E_x,E_y):
    for i in range(num_E):
        screen.blit(Enemy[i],(E_x[i],E_y[i]))

#making bullet
bullet = pygame.image.load('bullet.png')
bx = 0
by = 500
b_change = 1
b_state = False
b_shoot = False

def bullez(bx,by):
    if b_shoot is True:
        screen.blit(bullet,(bx,by))
        b_state = True

#score font
score = 0
defont = pygame.font.Font('impact.ttf',30)
font_x = 10
font_y = 5

def display(x,y):
    display_score = defont.render('Score: ' + str(score),True ,(255,255,255))
    screen.blit(display_score, (x,y))

#Collisions
def isCollide(bx,by,Ex,Ey):
        collision = math.sqrt((math.pow((bx-Ex),2))+math.pow((by-Ey),2))
        if collision < 60:
            return True
        else:
            return False

def isCollide2(main_x, main_y, Ex, Ey):
    collision = math.sqrt((math.pow((main_x - Ex), 2)) + math.pow((main_y - Ey), 2))
    if collision < 60:
        return True
    else:
        return False

#Game Over
font = pygame.font.Font('impact.ttf',100)
fontx = 175
fonty = 100

def game_over(x,y):
    GameOver = defont.render('Game Over',True ,(73, 89, 102))
    screen.blit(GameOver, (x,y))

#-----------------------------Main_Loops-------------------------------------#
while running:

    background()

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                main_change = -1
            if event.key == pygame.K_d:
                main_change = 1
            if event.key == pygame.K_SPACE:
                if b_state is False:
                    bx = main_x
                    by = main_y
                    b_shoot = True

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_a or
                    event.key == pygame.K_d or
                    event.key == pygame.K_SPACE):
                main_change = 0

        if event.type == pygame.QUIT:
            running = False


    for i in range(num_E):
        Over = isCollide2(main_x,main_y,E_x[i],E_y[i])
        if Over is True:
            for i in range(num_E):
                E_change[i] = 0
            game_over(fontx, fonty)
            break

        if Over is False:
            E_y[i] += E_change[i]
            if E_y[i]> 600:
                E_y[i] = 30

        Collide = isCollide(bx,by,E_x[i],E_y[i])
        if Collide is True:
            score += 10
            b_state = False
            by = 0
            E_y[i] = -10

    Eneme(E_x,E_y)

    main_x += main_change
    if main_x > 390:
        main_x =390
    if main_x < 20:
        main_x =20

    main_dest(main_x,main_y)

    if b_shoot is True:
        bullez(bx+14,by-20)
        by -= b_change
        b_state = True

    if by <0:
        b_state = False
        b_shoot = False
        by = 500

    display(font_x,font_y)

    pygame.display.update()




