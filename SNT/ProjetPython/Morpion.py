import numpy as np
import cv2
import keyboard
import time
import random
import pygame.mixer
 

def updateMobilePosition ():
    global mobile
    global direction
    global pas
    global hpas
    #Remove tail
    
    nbL,nbC = np.shape(mobile)
    l1 = (mobile[0,nbC-1])%sizeWindow
    l2 = (mobile[0,nbC-1] +pas-1)%sizeWindow
    c1 = (mobile[1,nbC-1])%sizeWindow
    c2 = (mobile[1,nbC-1] + pas-1)%sizeWindow
    img[l1:l2+1,c1:c2+1,0] = 0

    #UpdateBody
    mobile[:,1:nbC]=mobile[:,0:nbC-1]

    #Move Head
    if direction == 'up':
        mobile[0,0] = mobile[0,0]-pas
    elif direction == 'down':
        mobile[0,0] = mobile[0,0] +pas
    elif direction == 'left':
        mobile[1,0] = mobile[1,0] -pas
    elif direction == 'right':
        mobile[1,0] = mobile[1,0] +pas


    l1 = (mobile[0,0])%sizeWindow
    l2 = (mobile[0,0] +pas-1)%sizeWindow
    c1 = (mobile[1,0])%sizeWindow
    c2 = (mobile[1,0] +pas-1)%sizeWindow

    img[l1:l2+1,c1:c2+1,0] = 255

def putSugar():
    nbCase = sizeWindow/pas
    img[sugar[0,0]-10:sugar[0,0]+10,sugar[1,0]-10:sugar[1,0]+10,2] = 0
    l = (random.randint(0,nbCase)*pas +hpas )%sizeWindow
    c = (random.randint(0,nbCase)*pas +hpas)%sizeWindow
    sugar[0,0]=l
    sugar[1,0]=c
    img[l-10:l+10,c-10:c+10,2] = 255

def updateSugar():
    global score
    global pas
    global hpas
    if (mobile[0,0]+pas-1)%sizeWindow>=sugar[0,0] and (mobile[0,0])%sizeWindow<=sugar[0,0] and (mobile[1,0]+pas-1)%sizeWindow>=sugar[1,0]and  (mobile[1,0])%sizeWindow<=sugar[1,0]:
        putSugar()
        sonManger = pygame.mixer.Sound('sonManger.mp3')
        sonManger.play()
        score = score + 1
        img[20:121,390:601,1]=0
        cv2.putText(img, 'score : '+ str(score), (10,100), font, 3, (0, 255, 0), 2, cv2.LINE_AA)

        if score%1 == 0:

            mobileGrow()

def mobileGrow():
    global mobile
    global pas
    global hpas
    nbC = np.shape(mobile)[1]
    if direction == 'up':
        mobile = np.append(mobile, [[mobile[0,nbC-1]+pas], [mobile[1,nbC-1]]], axis=1)
    elif direction == 'down':
        mobile = np.append(mobile, [[mobile[0,nbC-1]-pas], [mobile[1,nbC-1]]], axis=1)
    elif direction == 'left':
        mobile = np.append(mobile, [[mobile[0,nbC-1]], [mobile[1,nbC-1]+pas]], axis=1)
    elif direction == 'right':
        mobile = np.append(mobile, [[mobile[0,nbC-1]], [mobile[1,nbC-1]-pas]], axis=1)
    l1 = (mobile[0,nbC])%sizeWindow
    l2 = (mobile[0,nbC] +pas-1)%sizeWindow
    c1 = (mobile[1,nbC])%sizeWindow
    c2 = (mobile[1,nbC] +pas-1)%sizeWindow
    img[l1:l2+1,c1:c2+1,0] = 255

def getFrame():
    updateSugar()
    updateMobilePosition()


def setDirection():
    global direction
    if keyboard.is_pressed("left") and direction!='right':
        direction = 'left'
    elif keyboard.is_pressed("right")and direction!='left':
        direction = 'right'
    elif keyboard.is_pressed("up")and direction!='down':
        direction = 'up'
    elif keyboard.is_pressed("down")and direction!='up':
        direction = 'down'

def checkIfDie():
    global gameOver
    global mobile
    mobile = mobile%sizeWindow
    nbC = np.shape(mobile)[1]
    condition1 = mobile[0,1:nbC]==mobile[0,0]
    condition2 = mobile[1,1:nbC]==mobile[1,0]
    if np.any(np.logical_and(condition1,condition2)):
        gameOver=True
        
pygame.mixer.init()     
pygame.mixer.music.load("musicMario.mp3")   # chargement de la musique
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

mobile = np.zeros((2,1),dtype = int)
sugar = np.zeros((2,1),dtype = int)
direction = 'right'
pas = int(50)
hpas = int(pas/2)
sizeWindow = 500
img = np.zeros((sizeWindow,sizeWindow,3),dtype = np.uint8)
putSugar()
cpt=0

score = 0
gameOver=False
imGameOver = cv2.imread('gameOver.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
la = 20
lb = 120
c1 = 390
c2 = 600

while (not keyboard.is_pressed('ctrl')) and not gameOver:

    setDirection()
    getFrame()
    checkIfDie()
    cv2.imshow('image',img)
    t1 = time.time()
    cv2.waitKey(100)
    t2 = time.time()
    print(t2-t1)
    

pygame.mixer.music.stop()  
if gameOver or keyboard.is_pressed('ctrl'):
    
   
   cv2.putText(imGameOver, 'score : '+ str(score), (50,210), font,2 , (0, 255, 0), 2, cv2.LINE_AA)
   cv2.imshow('image',imGameOver)
   sonGameOver= pygame.mixer.Sound('gameOver.mp3')
   sonGameOver.play()
   cv2.waitKey(5000)
pygame.mixer.stop()

pygame.mixer.quit()